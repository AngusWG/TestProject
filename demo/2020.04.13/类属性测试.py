#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2020/3/26 19:14
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : 类属性测试.py
import time


class A:
    class_list = []

    def __init__(self):
        self.class_list += [time.time()]

    def class_name(self):
        print(self.__class__.__name__)

    def register_event_source(self, *args):
        self.class_list += args

class B(A):
    pass


a = A()
b = B()
print(id(a.class_list))
print(id(b.class_list))
print(b.class_name())
