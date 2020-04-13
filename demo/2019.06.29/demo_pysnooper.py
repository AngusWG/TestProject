#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2019/5/20 12:53
# @Author  : zza
# @Email   : 740713651@qq.com



def cfunc():
    a = 0
    a += 1
    print(a)

import pysnooper
@pysnooper.snoop(depth=2)
def number_to_bits(number):
    cfunc()
    if number:
        bits = []
        while number:
            number, remainder = divmod(number, 2)
            bits.insert(0, remainder)
        return bits
    else:
        return [0]


number_to_bits(6)

# https://github.com/cool-RR/PySnooper
