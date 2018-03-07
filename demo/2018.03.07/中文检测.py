#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/3/5 0005 13:56
# @author  : zza
# @Email   : 740713651@qq.com
import re


def chinese(str):
    zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
    contents = str
    match = zhPattern.search(contents)

    if match:
        return match.group()
    else:
        return False


if __name__ == '__main__':
    print(chinese('我爱中国'))
    print(chinese('I love python.3.faf，中文'))
    print(chinese('我爱python'))
