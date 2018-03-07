#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/3/5 0005 15:33
# @author  : zza
# @Email   : 740713651@qq.com
import os

import sys


def getfilelist(param):
    # 列出目录下的所有文件和目录
    result = os.listdir(param)
    for item in result[::-1]:
        file = (param + "/" + item)
        if os.path.isdir(file):
            lower_item = getfilelist(file)
            result.remove(item)
            if lower_item is not None:
                add_item = {item: lower_item}
                result.append(add_item)
    if len(result) == 0:
        return None
    return result


def count_file_lines(file):
    if not file.endswith(".py"):
        return ""
    file = file[3:-3]
    if file.endswith("__init__"):
        return ""
    try:
        x = file.replace("/", ".")
        __import__(x)
        # print("*"*6)
        out = sys.stdout
        sys.stdout = open("help.txt", "a",encoding="utf8")
        help(x)
        sys.stdout.close()
        sys.stdout = out
        c=""
        print(c, "*" * 60)
        # print(c.find("\nDESCRIPTION"), c.find("DESCRIPTION") + 10)
        # c = c[c.find("\nDESCRIPTION"):c.find("DESCRIPTION")+10]
        return c
    except Exception as err:
        return ""


def get_doc(dirs, path):
    total_lines = ""
    for item in dirs:
        if isinstance(item, dict):
            item_path = list(item.keys())[0]
            item_dirs = list(item.values())[0]
            total_lines += get_doc(item_dirs, path + "/" + item_path)
        if isinstance(item, str):
            x = count_file_lines(path + "/" + item)
            total_lines += x if x else ""
    return total_lines


def get_doc_str(address):
    path = address
    # 获得文件目录树
    dirs = getfilelist(path)
    # 获得每个文件的行数
    num = get_doc(dirs, path)
    print(num)


if __name__ == '__main__':
    get_doc_str("..")
