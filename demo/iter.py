#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2019/5/22 10:31
# @Author  : zza
# @Email   : 740713651@qq.com


class A(list):
    def __iter__(self, *args, **kwargs):
        print("a")
        return super(A, self).__iter__(*args, **kwargs)

    def __next__(self):
        print("b")
        return super(A, self).__next__()


a = A()
a.append(1)
a.append(2)
a.append(3)

for i in a:
    print(i)
b = a.__iter__()
print(b.__next__())
print(b.__next__())
print(b.__next__())
