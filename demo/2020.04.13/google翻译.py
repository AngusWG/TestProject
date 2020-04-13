#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2019/12/13 15:11
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : google翻译.py

from googletrans import Translator

proxies = {"http": 'http://localhost:9999',
           "https": 'https://localhost:9999'}
translate = Translator(proxies=proxies)
result = translate.translate('请先登录')
print(result.text)
result = translate.translate('hello', dest='zh-CN')
print(result.text)
