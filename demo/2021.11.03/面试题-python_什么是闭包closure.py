#!/usr/bin/env python
# encoding: utf-8
# Created by zza on 2021/10/8 10:59
# Copyright 2021 LinkSense Technology CO,. Ltd
"""
from https://cloud.tencent.com/developer/article/1803643
def fun():
    temp = [lambda x: i*x for i in range(4)]
    return temp

for everyLambda in fun():
    print(everyLambda(2))
"""


def fun():
    temp = []
    for i in range(4):
        print("range i", i)

        def inner(x):
            print("inner i", i)
            return i * x

        temp.append(inner)
    return temp


for everyLambda in fun():
    print("everyLambda", everyLambda(2))
