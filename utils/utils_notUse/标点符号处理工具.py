#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/2/28 0028 11:52
# @author  : zza
# @Email   : 740713651@qq.com
import re


def punctuationToCN(var_str):
    var_str = re.subn(" +", " ", var_str)[0]
    var_str = var_str.replace(",", "，").replace(".", "。").replace("(", "（").replace(")", "）").replace(" ", "，").split("\n")
    res = ""
    for i in var_str:
        if i == "":
            res += "\n"
            continue
        if not i.endswith("。"):
            res += i + "。\n"
        else:
            res += i +"\n"
    return res


def main():
    a = """目的：
设计并实现一个电影推荐系统.
要求：
实现至少一个经典算法.
基于python语言

"""
    a = punctuationToCN(a)
    print(a)


if __name__ == '__main__':
    main()
