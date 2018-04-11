#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/3/24 0024 8:45
# @author  : zza
# @Email   : 740713651@qq.com


a = [1, 2, 3, 4, 5, 5, 6, 7, 8, 5, 5, 9, 65, 5, 5, 5, 5]

for i in a:
    if i == 5:
        a.remove(i)

print(a)


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

print(count())
for f in count():
    print(f())
