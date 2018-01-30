#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/1/24 0024 9:33
# @author  : zza
# @Email   : 740713651@qq.com
import os
import re
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
        elif not item.endswith(".py"):
            result.remove(item)
    if len(result) == 0:
        return None
    return result


def search_file(file, path, reg):
    a = open(path + "/" + file, 'U', encoding="utf-8").readlines()
    result = []
    for line in a:
        res = reg.findall(line)
        if not res == []:
            result.append(res)
    return {path + "/" + file: result, }


def do_search_dir(dirs, path, re_str):
    result = {}
    for item in dirs:
        if isinstance(item, dict):
            path_1 = list(item.keys())[0]
            filelist = list(item.values())[0]
            result.update(do_search_dir(filelist, path + "/" + path_1, re_str))
        else:
            res = search_file(item, path, re_str)
            if not list(res.values())[0] == []:
                result.update(res)

    return result


def result_processing1(result):
    for file in result:
        for str_1 in result[file]:
            for item in str_1:
                item = """msgid  ddd  \nmsgstr " "  """.replace("ddd", '"' + item + '"')
                output = open("./result.txt", "a")
                output.writelines(item + "\n" + "\n")


def result_processing(result):
    for item in result:
        item = """msgid  ddd  \nmsgstr " "  """.replace("ddd", '"' + item + '"')
        output = open("./result.txt", "a")
        output.writelines(item + "\n" + "\n")


def get_str(par_list):
    result = []
    if isinstance(par_list, dict):
        par_list = list(par_list.values())
    for item in par_list:
        if isinstance(item, str):
            result += [item]
            continue
        else:
            result += get_str(item)
    return result


def filter_processing(result, po_):
    str_list = get_str(result)
    # pprint(str_list)
    str_list = list(set(str_list))
    for i in str_list:
        if not isinstance(i, str) or len(i) == 1:
            pass
    a = open(po_, 'U', encoding="utf-8").readlines()
    re_str = r'msgid "(.*)"'
    reg = re.compile(re_str)
    str_list2 = []
    for item in a:
        res = reg.findall(item)
        if not res:
            continue
        for i in res:
            str_list2.append(i)
    for item in str_list[::-1]:
        if item in str_list2:
            str_list.remove(item)
    return str_list


def main():
    re_str = r'_\([\'\"](.*?)[\'\"]\)'
    reg = re.compile(re_str)
    path = "./kivy"
    dirs = getfilelist(path)
    result = do_search_dir(dirs, path, reg)
    po_ = r"E:\wallet\btcnano-wallet-client-desktop\lib\locale\zh_CN\electrum.po"
    result = filter_processing(result, po_)
    result_processing(result)


if __name__ == '__main__':
    main()
