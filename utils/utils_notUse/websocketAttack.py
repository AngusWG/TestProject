#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2017/12/20 0020 17:18
# @author  : zza
# @Email   : 740713651@qq.com
import websocket
from websocket import WebSocketApp


class AttackRobet(object):

    def __init__(self, url):
        self.url = url

    def get_ready(self,):
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp(self.url, on_open=on_open, on_message=on_message)
