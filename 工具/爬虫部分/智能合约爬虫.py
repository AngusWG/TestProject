#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/1/26 0026 9:15
# @author  : zza
# @Email   : 740713651@qq.com
import json
import re
import time
from pprint import pprint

import os
import requests
from requests import RequestException, ReadTimeout, ConnectTimeout, HTTPError


class logger:

    @classmethod
    def info(cls, param):
        logger.show_info("info", param)

    @classmethod
    def error(cls, err):
        logger.show_info("error", err)

    @classmethod
    def critical(cls, param):
        logger.show_info("critical", param)

    @classmethod
    def show_info(cls, tag, param):
        print(tag, param)


class RequestsHelper:
    """对requests请求进行简单封装, 请求时遇到浏览器验证自动处理cookies

    :from model import get_html: 一般调用可以直接这样用
    对requests的请求进行请求前的准备, 和请求后的异常处理
    """

    def __init__(self):
        self.user_agent = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36",
        }
        self.cookies = None

    def set_cookies_with_selenium(self, url, css_selector='form'):
        """ 用selenium访问传进来的url, 获取cookies, 目的是为了破解浏览器验证

        服务器上跑这段代码时可能会因为phantomjs出错, 可以按照README里面的方法安装phantomjs
        这里没有处理状态码不合格的情况
        :params url: url
        :params css_selector: css选择器, 当此此element不存在时才会认为通过了浏览器验证, 默认为from, 因为目前浏览器验证都有from
        :return: cookies
        """
        # 需要时才导入
        logger.info("get cookies with selenium")
        from selenium import webdriver
        from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.common.by import By
        from selenium.common.exceptions import TimeoutException

        # 设置UA
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = self.user_agent['User-Agent']
        try:
            # 这里的service_args存在疑问
            driver = webdriver.PhantomJS(desired_capabilities=dcap, service_args=['--ignore-ssl-errors=true'])
            if not (url.startswith('http://') or url.startswith('https://')):
                # 这个判断必须放在driver赋值之后
                raise ValueError('用于获取cookies的url格式不正确')
            driver.maximize_window()
            driver.get(url)

            time.sleep(10)
            # 等待, 直到 css_selector定位到的元素不存在
            res = WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, css_selector)))
            if res:
                self.cookies = {item['name']: item['value'] for item in driver.get_cookies()}
            else:
                raise ValueError('此url不能通过浏览器验证')
        except ValueError:
            raise ValueError
        except TimeoutException:
            # 网络超时, 重新请求
            self.set_cookies_with_selenium(url, css_selector=css_selector)
        except Exception as err:
            logger.error(err)

    def get_html(self, url, retry=10, timeout=60, method='get', **kwargs):
        """ 获取网页

        :params url: url
        :params retry: 发生网络错误重新执行的次数 默认10
        :params timeout: 超时秒数, 默认60
        :params method: 请求方法, 默认get
        :params args: 直接传入requests.request方法
        :params kwargs: 直接传入requests.request方法
        :return: `Response`; `url` If HTTPError  ; `False` If retry time > retry ;
        """
        if retry < 0:
            return False
        try:
            if 'headers' in kwargs:
                self.user_agent.update(kwargs.pop("headers"))
            resp = requests.request(url=url, headers=self.user_agent, timeout=timeout, method=method,
                                    cookies=self.cookies, **kwargs)
            resp.raise_for_status()
            # resp.encoding = resp.apparent_encoding

            if not hasattr(self, 'need_cookies'):
                # 第一次可以成功获得页面, 则不需要cookies
                self.need_cookies = False
            if resp is not None:
                return resp
            else:
                return self.get_html(url, retry - 1)
        except (ReadTimeout, ConnectTimeout, ConnectionError) as rcc:
            # 网络异常, 重新请求
            logger.error("网络出现异常, 重新请求: {}\r\n{}".format(url, rcc))
            return self.get_html(url, retry - 1)
        except HTTPError as err:
            if not hasattr(self, 'need_cookies'):
                # 第一次访问不可以成功获得页面, 默认为需要cookies
                self.need_cookies = True

            logger.critical("状态码错误: {}\r\n{}".format(url, err))

            if self.need_cookies:
                # 需要cookies, 重新请求
                self.temp_cookies = self.cookies
                self.set_cookies_with_selenium(url)

                # 当selenium请求页面之后, cookies没有改变, 说明不是cookies导致的状态码错误, 直接返回
                if self.cookies is not self.temp_cookies:
                    return self.get_html(url, retry - 1)

            # 状态码错误, 放弃该时间循环的请求
            return url

        except RequestException:
            # 不能处理的异常, 抛出
            logger.error('获取页面错误')
            raise RequestException


base_uri = "https://etherscan.io"


def get_test(url):
    res = RequestsHelper().get_html(url).text
    have_contract = re.findall(
        "</span><pre class='js-sourcecopyarea' id='editor' style='height: 330px; max-height: 450px; margin-top: 5px;'>([\s\S]*)</pre><br><script src='/jss/ace/ace.js' type='body/javascript' charset='utf-8'>",
        res)
    print(have_contract)
    if have_contract:
        have_contract = have_contract[0]
        return have_contract + "\r\r //" + url
    else:
        return


def getcontract(text):
    # print(body)
    res = re.findall("<a href='/address/(.*)'>", text)
    # print(res)
    res = "https://etherscan.io/address/" + res[0] + "#code"
    print(res)
    # res = get_test(res)
    return (res)


def save_contract(item):
    print(item)
    if item is None:
        return
    name = re.findall("ontract (.*) \{", item)[0]

    if not os.path.isdir(name):
        os.makedirs(name)
    file = open(name + "/" + name + ".sol", 'w',encoding="utf8")
    file.writelines(item)


def main():
    resp = RequestsHelper().get_html(base_uri + "/tokens").text
    res = re.findall("the Fintech revolution.</font></small></td>(.*)</td></tr>", resp)[0]
    res1 = re.findall("href='([/\w]*)'", res)
    res1 = list(set(res1))
    i = 0
    for x in res1:
        uri = base_uri + x
        i += 1
        # print(uri)
        save_contract(getcontract(RequestsHelper().get_html(uri).text))
        print(i / len(res1))


if __name__ == '__main__':
    main()
