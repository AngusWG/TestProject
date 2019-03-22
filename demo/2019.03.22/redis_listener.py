#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2019/3/22 10:58
# @Author  : zza
# @Email   : 740713651@qq.com
import redis

r = redis.Redis.from_url("redis://paladin:6380/2", decode_responses=True)
a = r.pubsub()
a.psubscribe("*")
with open("feeds.txt", 'a+') as f:
    for i in a.listen():
        if i['channel'] == 'tick_AG1906':
            f.write(str(i) + '\n')  # 加\n换行显示
# 发送
r.publish('a', 1)
