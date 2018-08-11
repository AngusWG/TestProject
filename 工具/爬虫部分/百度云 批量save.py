#!/usr/bin/python3
# encoding: utf-8 
# @author  : zza
# @Email   : 740713651@qq.com
# @Time    : 2018/8/11 0011
"""
批量从data.txt文件中读取百度云的url和密码
保存的上次的默认目录
百度云 
"""
from selenium import webdriver

user_cookies = "C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data"

option = webdriver.ChromeOptions()
option.add_argument(
    "--user-data-dir={}".format(user_cookies))  # 设置成用户自己的数据目录
browser = webdriver.Chrome(chrome_options=option)


def get_url_passwd(txt):
    with open(txt, "r", encoding="utf8")as f:
        lines = f.readlines()
    data = []
    for i in lines:
        if "pan.baidu.com" in i:
            i = i.replace("链接:", "")
            data.append(i.strip())

    res = []
    for i in data:
        url, passwd = i.split("密码:")
        res.append((url.strip(), passwd.strip()))
    if len(data) != len(res):
        raise Exception()
    return res


def save_2_baidu_cloud(url, passwd):
    print("start", url, passwd, end="")
    browser.get(url)
    browser.implicitly_wait(10)
    try:
        browser.find_element_by_xpath('//*[@class="clearfix"]/input').send_keys(passwd)
        browser.find_element_by_xpath('//*[contains(text(), "提取文件")]').click()
    except:
        pass
    browser.implicitly_wait(15)
    while True:
        try:
            browser.find_element_by_xpath('//*[contains(text(), "保存到网盘")]').click()
            browser.implicitly_wait(15)
            browser.find_element_by_xpath('//*[contains(text(), "最近保存路径")]').click()
            browser.find_element_by_xpath('//*[contains(text(), "确定")]').click()
            break
        except:
            print("get errer , try again .")
            continue
    browser.implicitly_wait(10)
    print(" over")
    # input()


def main():
    input_list = get_url_passwd("data.txt")
    i = 0
    for url, passwd in input_list:
        save_2_baidu_cloud(url, passwd)
        i += 1
        print("____________{}".format(i / len(input_list)))


if __name__ == '__main__':
    main()
