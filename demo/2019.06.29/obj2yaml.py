#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2019/6/10 16:45
# @Author  : zza
# @Email   : 740713651@qq.com
import os

import yaml


class Config:
    LOG_PATH = '/logs/demo/demo_server.log'
    SCHEDULER_LOG_PATH = '/logs/demo/demo_scheduler.log'
    LOG_MAXBYTES = 10000
    LOG_BACKCOUNT = 10

    def __init__(self):
        if not os.path.exists("config.yaml"):
            return
        with open("config.yaml", 'r', encoding="utf8") as f:
            entries = yaml.load(f)
        self.__dict__.update(entries)


conf = Config()
obj = {k: conf.__getattribute__(k) for k in dir(conf) if k.isupper()}
file = '{}.yaml'.format(os.getenv('DEMO_ENV'))
stream = open(file, 'w')
print(yaml.safe_dump(obj, stream=stream, default_flow_style=False, encoding='utf-8', allow_unicode=True))
