#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/1/10 0010 15:09
# @author  : zza
# @Email   : 740713651@qq.com

# !/usr/bin/env python
# -*- coding: utf-8 -*-
import kivy
from kivy.app import App
from kivy.uix.label import Label

__version__ = '0.1'


class MyApp(App):
    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':
    MyApp().run()

