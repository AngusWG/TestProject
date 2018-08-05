#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/7/6 0006 15:06
# @author  : zza
# @Email   : 740713651@qq.com

import pickle

test_data = ['Save me!', 123, 'ss', True]
t1 = pickle.dumps(test_data)
print(t1)
#     b'\x80\x03]q\x00(X\x08\x00\x00\x00Save me!q\x01K{X\x02\x00\x00\x00ssq\x02\x88e.'

t2 = pickle.loads(t1)
print(t2)
#    ['Save me!', 123, 'ss', True]


a_dict = {'da': 111, 2: [23, 1, 4], '23': {1: 2, 'd': 'dad'}}

# 保存
file = open('pickle_example.pickle', 'wb')
pickle.dump(a_dict, file)
file.close()

# 读取
file = open('pickle_example.pickle', 'rb')
a_dict1 = pickle.load(file)
file.close()
print(a_dict1)
