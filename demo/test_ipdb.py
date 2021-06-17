#!/usr/bin/env python
# encoding: utf-8
# Created by zza on 2021/5/20 16:54
# Copyright 2021 LinkSense Technology CO,. Ltd

import ipdb


def server():
    a = 2
    b = 3
    print(a + b)
    ipdb.set_trace()
    return a * b


if __name__ == '__main__':
    server()
