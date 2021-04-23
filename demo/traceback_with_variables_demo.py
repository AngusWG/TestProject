#!/usr/bin/env python
# encoding: utf-8
# Created by zza on 2021/4/22 19:26
# Copyright 2021 LinkSense Technology CO,. Ltd

# noinspection PyUnresolvedReferences
from traceback_with_variables import activate_by_import


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
