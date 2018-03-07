#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/2/24 0024 11:04
# @author  : zza
# @Email   : 740713651@qq.com
import pymongo
import copy

from utils import strUtils

db = pymongo.MongoClient('192.168.14.240', 27017)["smart_contract"]
table = db["Function"]


def bak():
    txt = ""
    for i in table.find({}):
        txt += str(i) + "\n"
    f = open("bak.txt", "+w", encoding="utf8")
    f.write(txt)
    f.close()


def dosth():
    for i in table.find({}):
        x = copy.deepcopy(i)
        for k in i.keys():
            if k == "_id":
                continue
            text = i[k]
            i[k] = strUtils.punc_to_zh_cn(text)
        if not str(i) == str(x):
            print(i)
            print(x)
            print()
            # table.delete_one(x)
            # table.insert_one(i)


if __name__ == '__main__':
    dosth()
    pass
