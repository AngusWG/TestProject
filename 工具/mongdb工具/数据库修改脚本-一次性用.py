#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/2/24 0024 11:04
# @author  : zza
# @Email   : 740713651@qq.com
import pymongo

db1 = pymongo.MongoClient('192.168.14.240', 27017)["smart_contract"]
db2 = pymongo.MongoClient('www.xxx.cn', 27017)["smart_contract"]


def 数据库迁移():
    for table in db1.collection_names():
        for item in db1[table].find():
            db2[table].update({"_id": item["_id"]}, {"$set": item}, upsert=True,check_keys=False)


def dosth():
    pass


if __name__ == '__main__':
    数据库迁移()
    pass
