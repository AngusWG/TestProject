#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2021/11/3 10:55
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : t_unix_socket.py
import socket
import sys


def socket_client():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 61662))
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print(s.recv(1024))  # 目的在于接受：Accept new connection from (...
    while 1:
        data = input('please input work: ').encode()
        s.send(data)
        print('aa', s.recv(1024))
        if data == b'exit':
            break
    s.close()


if __name__ == '__main__':
    socket_client()
