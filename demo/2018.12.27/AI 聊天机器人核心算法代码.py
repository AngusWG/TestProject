#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2019/1/18 9:58
# @Author  : zza
# @Email   : 740713651@qq.com


def get_answer(param):
    return param.replace("吗", "").replace("?", "!")


def server():
    while True:
        print(get_answer(input()))


if __name__ == '__main__':
    server()
