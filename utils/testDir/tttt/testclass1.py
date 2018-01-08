#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2017/12/19 0019 11:41
# @author  : zza
# @Email   : 740713651@qq.com
import pymongo

mongoDB = pymongo.MongoClient("127.0.0.1", 27017)
# 获得交易所列表
ex_list = []
for i in mongoDB["History_exchange"]["exchanges"].find():
    ex_list.append(i["name"])

ex_num = 0
for ex in ex_list:
    ex_num += 1
    # 获得每个交易所的币种
    cu_list = mongoDB[ex].collection_names()
    cu_num = 0
    for cu in cu_list:
        cu_num += 1
        items = mongoDB[ex][cu].find()
        filename = ex + "_" + cu.replace("/", ".")
        f = open(filename, "w")
        for i in items:
            f.write(str(i) + "\n")
        f.close()
        print("\r*  {}%  {}% ".format(ex_num / len(ex_list)*100, cu_num / len(cu_list)*100), end="")
