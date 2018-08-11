#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/7/18 0018 10:56
# @author  : zza
# @Email   : 740713651@qq.com
from prompt_toolkit import prompt

if __name__ == '__main__':
    answer = prompt('Give me some input: ')
    print('You said: %s' % answer)
