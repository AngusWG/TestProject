#!/usr/bin/python3
# encoding: utf-8
# @Time    : 2021/11/3 10:55
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : t_unix_socket.py
# -*- coding: utf-8 -*-
import os.path
import socket

if os.path.exists("/tmp/python_unix_sockets_example"):
    os.remove("/tmp/python_unix_sockets_example")

print("Opening socket...")
server = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server.bind("/tmp/python_unix_sockets_example")

print("Listening...")
while True:
    datagram = server.recv(1024)
    if not datagram:
        break
    else:
        print("-" * 20)
        print(datagram)
        if "DONE" == datagram:
            break
print("-" * 20)
print("Shutting down...")
server.close()
os.remove("/tmp/python_unix_sockets_example")
print("Done")
