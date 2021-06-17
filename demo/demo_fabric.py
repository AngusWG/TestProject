#!/usr/bin/env python
# encoding: utf-8
# Created by zza on 2021/6/10 11:10
# Copyright 2021 LinkSense Technology CO,. Ltd

# https://www.jb51.net/article/164552.htm
from fabric import Connection

result = Connection('root@192.168.0.122', connect_kwargs={"password": "1111"}).run('uname -s', hide=True)
msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"
print(msg.format(result))
