#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/4/12 0012 16:54
# @author  : zza
# @Email   : 740713651@qq.com

# -*- coding: utf-8 -*-
from pprint import pprint

import requests
from lxml import etree


def get_proxies_from_site():
    url = 'http://proxy.ipcn.org/country/'
    xpath = '/html/body/div[last()]/table[last()]/tr/td/text()'

    r = requests.get(url)
    tree = etree.HTML(r.text)

    results = tree.xpath(xpath)
    proxies = [line.strip() for line in results]

    return proxies


# 使用http://lwons.com/wx网页来测试代理主机是否可用
def get_valid_proxies(proxies, count):
    url = 'https://www.douban.com'
    results = []
    cur = 0
    print("代理列表:")
    print(proxies)
    print("测试代理:")

    for p in proxies:
        proxy = {'http': 'http://' + p}
        succeed = False
        try:
            r = requests.get(url, proxies=proxy)
            if r.status_code == 200:
                succeed = True
        except Exception as e:
            print('error:', p)
            succeed = False
        if succeed:
            print('succeed:', p)
            results.append(p)
            cur += 1
            if cur >= count:
                break
    return results


if __name__ == '__main__':
    list = get_valid_proxies(get_proxies_from_site(), 20)
    print('get ' + str(len(list)) + ' proxies')
    pprint(list)
