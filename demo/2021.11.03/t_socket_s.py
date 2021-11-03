#!/usr/bin/python3
# encoding: utf-8
# @Time    : 2021/11/3 10:55
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : t_unix_socket.py
"""
file: service.py
socket service
"""

import socket
import sys
import threading
import time


def socket_service():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 防止socket server重启后端口被占用（socket.error: [Errno 98] Address already in use）
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('127.0.0.1', 61662))
        s.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print('Waiting connection...')

    while 1:
        conn, addr = s.accept()
        t = threading.Thread(target=deal_data, args=(conn, addr))
        t.start()


def deal_data(conn, addr):
    print('Accept new connection from {0}'.format(addr))
    conn.send(('Hi, Welcome to the server!').encode())
    while 1:
        data = conn.recv(1024)
        print('{0} client send data is {1}'.format(addr,
                                                   data.decode()))  # b'\xe8\xbf\x99\xe6\xac\xa1\xe5\x8f\xaf\xe4\xbb\xa5\xe4\xba\x86'
        time.sleep(1)
        if data == 'exit' or not data:
            print('{0} connection close'.format(addr))
            conn.send(bytes('Connection closed!'), 'UTF-8')
            break
        conn.send(bytes('Hello, {0}'.format(data), "UTF-8"))  # TypeError: a bytes-like object is required, not 'str'
    conn.close()


if __name__ == '__main__':
    socket_service()
