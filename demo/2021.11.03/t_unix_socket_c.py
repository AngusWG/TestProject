#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2021/11/3 10:55
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : t_unix_socket.py
# -*- coding: utf-8 -*-
import socket
import os, os.path

print("Connecting...")
if os.path.exists("/tmp/python_unix_sockets_example"):
    client = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    client.connect("/tmp/python_unix_sockets_example")
    print("Ready.")
    print("Ctrl-C to quit.")
    print("Sending 'DONE' shuts down the server and quits.")
    while True:
        try:
            x = input("> ")
            if "" != x:
                print("SEND:", x)
                client.send(x.encode())
                if "DONE" == x:
                    print("Shutting down.")
                    break
        except KeyboardInterrupt:
            print("Shutting down.")
    client.close()
else:
    print("Couldn't Connect!")
print("Done")
