#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2021/4/4 17:05
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : c.py
from functools import partial


class F(partial):
    def __ror__(self, other):
        print("self",self)
        print("other", other)
        ret = self(other)
        print("ret", ret)
        return ret


a = range(10) | F(filter, lambda x: x % 2) | F(sum)
print(a)
