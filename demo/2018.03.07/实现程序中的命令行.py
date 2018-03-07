#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/3/5 0005 14:13
# @author  : zza
# @Email   : 740713651@qq.com

import sys
def fun1(s):
    print(s * 5)


def main():
    """#
    >>> fun1(5)
    25
    """
    while True:
        a = input("op:")
        c = eval(a)
        print(type(c), c)
        pass


if __name__ == '__main__':
    main()
