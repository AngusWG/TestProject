#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/7/6 0006 15:02
# @author  : zza
# @Email   : 740713651@qq.com

from retrying import retry


def wait_func(*args, **kwargs):
    print(args, kwargs)
    return 3


@retry(wait_func=wait_func, stop_max_attempt_number=5)
def a(c=None):
    print(c)
    return dict()[5]


a(5)
