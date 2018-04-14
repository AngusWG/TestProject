#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/3/24 0024 8:41
# @author  : zza
# @Email   : 740713651@qq.com


def bug_one():
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


def fun1(a):
    a += a
    print(id(a))


def fun2(a):
    a = a + a
    print(id(a), a)


def bug_two():
    a = 1
    fun1(a)
    print(id(a))
    a = [1, 2]
    print(id(a), a)
    fun1(a)
    print(id(a), a)
    print("*" * 60)
    a = [1, 2]
    print(id(a), a)
    fun2(a)
    print(id(a), a)


if __name__ == '__main__':
    bug_one()
    bug_two()
