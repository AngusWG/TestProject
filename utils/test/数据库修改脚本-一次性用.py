#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/2/24 0024 11:04
# @author  : zza
# @Email   : 740713651@qq.com
import pymongo
import copy

db = pymongo.MongoClient('192.168.14.240', 27017)["smart_contract"]
table = db["Contract"]
for i in table.find({}):
    # if not " is " in i["_id"]:
    #     continue
    # x = copy.deepcopy(i)
    # text = i["_id"]
    # i["_id"] = i["_id"][:text.find(" is ")]
    # table.delete_one(x)
    # table.insert_one(i)
    print(i)
