#!/usr/bin/env python
# encoding: utf-8
# Created by zza on 2021/6/17 15:53
# Copyright 2021 LinkSense Technology CO,. Ltd
from datetime import datetime

code = """
import datetime



class DefineByMyself:
    def __init__(self):
        self.time = datetime.datetime.now()
        super(DefineByMyself, self).__init__()
"""


def init_class(class_name='DefineByMyself'):
    local_vars = globals().copy()
    exec(code, local_vars, local_vars)
    item = local_vars[class_name]()
    print(item.time)
    print(datetime.now())


def init_class2(class_name='DefineByMyself'):
    local_vars = globals()
    exec(code, globals(), local_vars)
    item = local_vars[class_name]()
    print(item.time)
    print(datetime.now())  # get error datetime = datetime.datetime


if __name__ == '__main__':
    print(globals().keys())
    init_class()
    print(globals().keys())
