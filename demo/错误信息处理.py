#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/7/20 0020 9:45
# @author  : zza
# @Email   : 740713651@qq.com
import re

a = ""
with open("crawler_error.log", encoding="utf8") as f:
    a = "".join(f.readlines())
c = re.findall("SQL: '[^\]]+", a)
for i in c:
    print(i)

print("*" * 60)
c = sorted(set(c))
for i in c:
    print(i.replace("\\n", "\n "))
    print()
