#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/1/19 0019 9:20
# @author  : zza
# @Email   : 740713651@qq.com
import os
import pprint
import difflib

import sys


def getfilelist(param):
    # 列出目录下的所有文件和目录
    result = os.listdir(param)
    # add_list = list()
    for item in result[::-1]:
        file = (param + "/" + item)
        if os.path.isdir(file):
            lower_item = getfilelist(file)
            result.remove(item)
            if lower_item is not None:
                add_item = {item: lower_item}
                result.append(add_item)
        # elif not item.endswith(".py"):
        #     result.remove(item)
    if len(result) == 0:
        return None
    return result


diff = difflib.HtmlDiff()


def compare_two_dir(newdir, new_path, old_path):
    for item in newdir:
        if isinstance(item, dict):
            path = list(item.keys())[0]
            filelist = list(item.values())[0]
            compare_two_dir(filelist, new_path + "/" + path, old_path + "/" + path)
        else:
            try:
                a = open(new_path + "/" + item, 'U', encoding="utf-8").readlines()
                b = open(old_path + "/" + item, 'U', encoding="utf-8").readlines()
                result = diff.make_file(a, b, context=True)
                print(result)
                # print(new_path + "/" + item)
                if "No Differences Found" in result:
                    continue
                print(item+".html")
                output = open( item+".html", "w+")
                # output = open("./result/" + item+".html", "w+")
                output.writelines(new_path + "/" + item + "\n")
                output.write(result)
                output.close()
            except FileNotFoundError as e:
                pass


def main():
    # new_dirs = getfilelist("./Bitcoin-Nano")
    old_dir = input("老文件夹地址:")
    print()
    new_dir = input("新文件夹地址:")
    # old_dirs = getfilelist("./btcnano-1.0")
    # compare_two_dir(old_dirs, "./Bitcoin-Nano", "./btcnano-1.0")
    print(old_dir, new_dir)
    old_dirs = getfilelist(old_dir)
    compare_two_dir(old_dirs, new_dir, old_dir)

    input("get a key to close")


if __name__ == '__main__':
    main()
    # pprint.pprint(getfilelist("./Bitcoin-Nano"))
