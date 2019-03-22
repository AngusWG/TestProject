#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2019/3/18 17:24
# @Author  : zza
# @Email   : 740713651@qq.com
import random

_set = set(random.random() for i in range(50000))
_list = list(_set)
_tuple = tuple(_set)
_x = set(random.random() for i in range(300))


def func1(iter, a):
    for i in a:
        if a in iter:
            return True


func1(_set, _x) == func1(_list, _x) == func1(_tuple, _x)
