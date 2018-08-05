#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/7/6 0006 14:56
# @author  : zza
# @Email   : 740713651@qq.com

from time import sleep

from tqdm import tqdm

for i in tqdm(range(500)):
    # print("\r" + '*' * i, end="")
    sleep(0.01)
for i in range(500):
    print("\r" + '*' * i, end="")
    sleep(0.01)
