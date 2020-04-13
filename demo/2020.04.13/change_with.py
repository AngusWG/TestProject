#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2020/4/8 10:55
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : change_with.py
from threading import Lock

import pysnooper

_lock = Lock()


@pysnooper.snoop('file.log')
class A:
    def _enter(self):
        with _lock:
            print(112233)
            print(222)
        return True

    def p(self):
        print(1212)


A()._enter()

# @pysnooper.snoop('file.log')
