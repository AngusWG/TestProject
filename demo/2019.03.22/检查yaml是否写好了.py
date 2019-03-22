#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2019/2/19 18:26
# @Author  : zza
# @Email   : 740713651@qq.com
import yaml

r = open("config.yaml", "r", encoding="utf8")
a = r.read()
print(yaml.load(a)["data"]["config.py"])
