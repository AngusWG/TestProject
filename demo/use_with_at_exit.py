#!/usr/bin/env python
# encoding: utf-8
# Created by zza on 2021/3/10 18:27
# Copyright 2021 LinkSense Technology CO,. Ltd
import atexit


@atexit.register
def clean():
    print("清理数据")


def main():
    1/0


if __name__ == '__main__':
    main()

