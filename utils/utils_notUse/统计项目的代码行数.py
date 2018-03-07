#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/2/1 0001 15:11
# @author  : zza
# @Email   : 740713651@qq.com
import os
from pprint import pprint


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
    if len(result) == 0:
        return None
    return result


def count_file_lines(file):
    try:
        count = len(open(file, 'r', encoding="utf8").readlines())
        if count > 1000:
            print(count, file)
        return count
    except:
        return 0


def count_lines(dirs, path):
    total_lines = 0
    for item in dirs:
        if isinstance(item, dict):
            item_path = list(item.keys())[0]
            item_dirs = list(item.values())[0]
            total_lines += count_lines(item_dirs, path + "/" + item_path)
        if isinstance(item, str):
            total_lines += count_file_lines(path + "/" + item)
    return total_lines


def main():
    path = "E:\pythonCode\smart_contract_test\\bean"
    # 获得文件目录树
    dirs = getfilelist(path)
    # 获得每个文件的行数
    num = count_lines(dirs, path)
    print(num)


if __name__ == '__main__':
    main()
