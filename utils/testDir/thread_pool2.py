#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2017/12/23 0023 11:00
# @author  : zza
# @Email   : 740713651@qq.com

# -*- coding=utf-8 -*-
import threadpool
import time


def Main_Def(par1, par2, par3):
    print("par1 = %s, par2 = %s, par3 = %s" % (par1, par2, par3))


if __name__ == '__main__':
    # 方法1
    list_var1 = ['1', '2', '3']
    # 方法2
    # dict_var1 = {'par1': '1', 'par2': '2', 'par3': '3'}
    # dict_var2 = {'par1': '4', 'par2': '5', 'par3': '6'}
    # par_list = [(None, dict_var1), (None, dict_var2)]
    request = threadpool.WorkRequest(Main_Def, list_var1)

    pool = threadpool.ThreadPool(2)
    # requests = threadpool.makeRequests(Main_Def, par_list)
    pool.putRequest(request)
    time.sleep(1)
    pool.wait()
    a = 1
    while True:
        a += 1
        if a==2000000:
            break
