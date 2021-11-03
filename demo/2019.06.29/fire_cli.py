#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2019/4/23 10:09
# @Author  : zza
# @Email   : 740713651@qq.com
"""python fire_cli.py say_hello 1423 35 0"""
import fire


def say_hello(name: str = '2ada', k: str = "", f: int = 0):
    print("type(name)", type(name))
    print(name, k, f)
    return 'Hello {}!'.format(name)


if __name__ == '__main__':
    fire.Fire()
