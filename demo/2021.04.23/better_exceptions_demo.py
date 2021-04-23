#!/usr/bin/env python
# encoding: utf-8
# Created by zza on 2021/4/23 14:38
# Copyright 2021 LinkSense Technology CO,. Ltd

import better_exceptions

better_exceptions.encoding.ENCODING = 'utf8'
better_exceptions.hook()


def func2(a, b):
    b = b + 1
    d = 23
    c = a / b
    return c


def func1():
    a = 1
    b = -1
    a += 32
    return func2(a, b)


func1()
