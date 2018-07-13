#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/7/11 0011 17:40
# @author  : zza
# @Email   : 740713651@qq.com
import json


def load_table():
    try:
        with open("非小号关系对应表.txt", 'r') as f:
            info = f.readlines()
            return json.loads("".join(info))
    except FileNotFoundError:
        return {}


def save_table(tab):
    with open("非小号关系对应表.txt", 'w') as f:
        f.writelines(json.dumps(tab))
    return True


print(load_table())
save_table({12:564})