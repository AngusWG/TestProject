#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2019/7/30 16:07
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : redis_ttt.py


import redis

r = redis.Redis.from_url("redis://127.0.0.1:6379/2")
tick_ps = r.pubsub()
tick_ps.subscribe('tick_{}'.format("A1805"))
while True:
    a = tick_ps.get_message(ignore_subscribe_messages=False, timeout=0.1)
    if a is not None:
        print(a)

##

import redis
import time

r = redis.Redis.from_url("redis://127.0.0.1:6379/2")
tick_ps = r.pubsub()
while True:
    time.sleep(1)
    r.publish('tick_{}'.format("A1805"), int(time.time()))
    r.publish('tick_{}'.format("A1807"), int(time.time()))
