#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2019/3/10 15:01
# @Author  : zza
# @Email   : 740713651@qq.com

import numba as nb
import numpy as np

# 普通的 for


def add1(x, c):
    rs = [0.] * len(x)
    for i, xx in enumerate(x):
        rs[i] = xx + c
    return rs


# list comprehension
def add2(x, c):
    return [xx + c for xx in x]


# 使用 jit 加速后的 for
@nb.jit(nopython=True)
def add_with_jit(x, c):
    rs = [0.] * len(x)
    for i, xx in enumerate(x):
        rs[i] = xx + c
    return rs


y = np.random.random(10 ** 5).astype(np.float32)
x = y.tolist()

import random
import numba as nb
from interval import Interval


def keep_error_time(time):
    return 200000000 < time <= 202900000 or 80000000 < time <= 85900000


int_20_20 = Interval(200000000, 202900000)
int_08_08 = Interval(80000000, 85900000)


def keep_error_time_2(time):
    return time in int_20_20 or time in int_08_08


@nb.jit(nopython=True)
def keep_error_time_3(time):
    return 200000000 < time <= 202900000 or 80000000 < time <= 85900000


times = [random.randint(80000000, 85900000) for i in range(10 ** 5)]
assert [keep_error_time(time) == keep_error_time_2(time) for time in times]
"""
%timeit  [keep_error_time(time)for time in times ]
%timeit  [keep_error_time_2(time) for time in times ]
%timeit  [keep_error_time_3(time) for time in times ]
"""

assert np.allclose(add1(x, 1), add2(x, 1), add_with_jit(x, 1))
"""
%timeit add1(x, 1)
%timeit add2(x, 1)
%timeit add_with_jit(x, 1)
"""
