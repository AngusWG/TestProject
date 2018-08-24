#!/usr/bin/python3
# encoding: utf-8 
# @author  : zza
# @Email   : 740713651@qq.com
# @Time    : 2018/8/23 0023
import os

import requests
from lxml import etree

print("运行前请在当前目录下创建 zips 文件夹")
#
# names = []
# url = 'https://github.com/UlordChain?language=&page={}&q=&type=&utf8=%E2%9C%93'.format(1)
# selector = etree.HTML(requests.get(url).text)
# names = names + selector.xpath('//*[@id="org-repositories"]/div[1]/div/li/div/h3//@href')
# url = 'https://github.com/UlordChain?language=&page={}&q=&type=&utf8=%E2%9C%93'.format(2)
# selector = etree.HTML(requests.get(url).text)
# names = names + selector.xpath('//*[@id="org-repositories"]/div[1]/div/li/div/h3//@href')
#
# print(len(names), "个项目需要下载")
# for i in names[:1]:
#     url = 'https://github.com{}/archive/master.zip'.format(i)
#     s = requests.get(url, stream=True)
#     print(i)
#     with open("zips" + i[i.rfind("/"):] + ".zip", "wb") as f:
#         # print(i)
#         for i in s:
#             print("..", end="")
#             f.write(i)


def find_and_move(path, to_path):
    res = os.listdir(path)
    for i in res:
        a = os.path.join(path, i)
        if os.path.isdir(a):
            find_and_move(a, to_path)
            if len(os.listdir(a)) == 0:
                os.rmdir(a)
        else:
            if not a.endswith(".md"):
                print("remove ", a)
                os.remove(a)


# print()
# print("请手动解压，解压后命令行敲enter键")
# input()
res = os.listdir("zips")
for i in res:
    a = os.path.join("zips", i)
    if os.path.isdir(a):
        print("get dir", i)
        find_and_move(a, a)
