#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2020/11/2 22:50
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : reduce_tmp.py
from functools import reduce


def add(x, y):  # 两数相加
    print("x", x)
    print("y", y)
    return x + y


reduce(add, [1, 2, 3, 4, 5])  # 计算列表和：1+2+3+4+5

reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
