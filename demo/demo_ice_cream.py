#!/usr/bin/python3
# encoding: utf-8
# @Time    : 2021/9/15 10:54
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : tmp.py
"""
github: https://github.com/gruns/icecream

"""
from icecream import ic


def foo(i):
    return i + 333


ic(foo(123))
