#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/2/24 0024 11:04
# @author  : zza
# @Email   : 740713651@qq.com
import pymongo
import copy

# db = pymongo.MongoClient('192.168.14.241', 27017)["smart_contract"]
table = db["Function"]
for i in table.find():
    # if not i["_id"].startswith(" "):
    #     continue
    x = copy.deepcopy(i)
    i["type"]= i["_id"].split()[0]
    table.delete_one(x)
    table.insert_one(i)
