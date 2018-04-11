#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/3/24 0024 8:41
# @author  : zza
# @Email   : 740713651@qq.com


def fun1(a):
    a += a
    print(id(a))


def fun2(a):
    a = a + a
    print(id(a),a)


if __name__ == '__main__':
    a = 1
    fun1(a)
    print(id(a))
    a = [1, 2]
    print(id(a),a)
    fun1(a)
    print(id(a),a)
    print("*" * 60)
    a = [1, 2]
    print(id(a),a)
    fun2(a)
    print(id(a),a)
