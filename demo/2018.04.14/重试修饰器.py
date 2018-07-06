#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/7/6 0006 15:02
# @author  : zza
# @Email   : 740713651@qq.com
import time


def do_something():
    pass


for i in range(5):
    try:
        do_something()
        break
    except:
        time.sleep(2)

from retry import retry


@retry(tries=5, delay=2)
def do_something():
    pass


do_something()
