#encoding: utf-8
import pymongo

HOST = "www.4yewu.cn"
PORT = 27017

client = pymongo.MongoClient(HOST, PORT)

doubanDB = client.douban