#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2021/8/24 13:56
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : demo_redislite.py
from redislite import Redis
redis_connection = Redis('./redis.db')
redis_connection.keys()
[]
redis_connection.set('key', 'value')
True
redis_connection.get('key')
'value'
