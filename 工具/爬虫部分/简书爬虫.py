#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/6/22 23:47 
# @author  : zza
# @Email   : 740713651@qq.com
"""
简书爬虫
只是将某作者的文章粗糙的转换为txt文件  方便作者手机语音朗读
从url中获得作者的连接的id部分
然后填入authors的list就行了
"""
import os

import requests
from lxml import etree

header = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}

import re


def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    return new_title


def 获得文章(url):
    # url = '/p/fb35df00f134'
    url = 'https://www.jianshu.com' + url
    req1 = requests.get(url, headers=header)
    selector = etree.HTML(req1.text)
    name = selector.xpath('/html/body/div[1]/div[1]/div[1]/h1//text()')[0]
    text = selector.xpath('/html/body/div[1]/div[1]/div[1]/div[2]//text()')
    return name, url + "".join(text)


def 保存文章(author, name, text):
    name = validateTitle(name)
    with open('./' + author + '/' + name + ".txt", 'w', encoding="utf8") as f:
        f.write(text)
    return True


def 获得作者文章列表(name):
    name = '960610ad2f98'
    i = 0
    res_list = set()
    num = -1
    while len(res_list) != num:
        num = len(res_list)
        i += 1
        req1 = requests.get('https://www.jianshu.com/u/' + name + '?order_by=shared_at&page=' + str(i), headers=header)
        selector = etree.HTML(req1.text)
        [res_list.add(i) for i in selector.xpath('//*[@id="list-container"]//li/div/a/@href')]
    return list(res_list)


if __name__ == '__main__':
    print("开始爬")
    authors = ['55b0ef58a213']
    for author in authors:
        folder = os.path.exists("./" + author)
        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs("./" + author)
        print('正在爬{}作者的文章'.format(author))
        file_lisr = 获得作者文章列表(author)
        for f in file_lisr:
            print("正在获得文章", f)
            name, text = 获得文章(f)
            保存文章(author, name, text)
