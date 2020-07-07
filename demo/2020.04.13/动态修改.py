#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2020/2/21 11:28
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : 动态修改.py
import types


class A:
    def __init__(self):
        self.a = 1

    def p(self, num):
        print("A", self.a)
        print("num", num)
        print("*" * 20)


def p(num):
    print("B", None)
    print("num", num)
    print("*" * 20)


def p1(self, num):
    print("C", self.a)
    print("num", num)
    print("*" * 20)


a = A()
a.p = p
a.p(1)

a.p = types.MethodType(p1, a)
a.p(2)

b = A()
b.__class__.p = p1
b.p(3)


def init_2(self):
    print("init_2")
    self.a = 1


A.__init__ = init_2
c = A()
c.p(3)
