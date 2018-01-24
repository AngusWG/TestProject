#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/1/8 0008 17:26
# @author  : zza
# @Email   : 740713651@qq.com
import sys, os

import pymongo

mongoDB = pymongo.MongoClient("127.0.0.1", 27017)


def get_file_name():
    dir = "./data"
    fielnum = 0
    list = os.listdir(dir)  # 列出目录下的所有文件和目录
    re_list = {}
    for filename in list:
        filename1 = filename.replace(".", "/")
        file, t = filename1.split("_", 1)
        print(file, t)
        if not re_list.get(file):
            re_list[file] = []
        re_list[file].append((filename, t))

    print(re_list)
    return re_list


def main():
    table = get_file_name()
    for ex in table:
        db = mongoDB[ex]
        for file, msg_type in table[ex]:
            with open("./data/" + file) as fh:
                try:
                    for line in fh:
                        print(line)
                        db[msg_type].insert_one(eval(line))
                except:
                    pass


if __name__ == '__main__':
    main()
