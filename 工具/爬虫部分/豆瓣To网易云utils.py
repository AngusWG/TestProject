#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/6/25 0025 13:06
# @author  : zza
# @Email   : 740713651@qq.com

import os
import re
import json
import requests
from lxml import etree
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4882.400 QQBrowser/9.7.13059.400",
    "Cookie":
        '_pk_id.100002.6447=716173b3686833a6.1524918275.1.1524918275.1524918275.; _ga=GA1.2.1739038372.1524918275; bid=bgmmtinYYSw; flag="ok"; dbcl2="52357979:CEk+opmv16U"; ck=NHNN; _gid=GA1.2.1847158917.1530113150; _gat=1'
}

req1 = requests.get('https://douban.fm/j/v2/redheart/basic', headers=header)
body = json.loads(req1.text)['songs']
service_args = ['--ignore-ssl-errors=true',
                # '--proxy=119.41.168.186:53281', '--proxy-type=https',
                '--ssl-protocol=TLSv1']
dcap = dict(DesiredCapabilities.PHANTOMJS)
driver = webdriver.PhantomJS(executable_path="phantomjs.exe", service_args=service_args,
                             desired_capabilities=dcap)
driver.co


def 豆瓣获得所有歌():
    songs = {}
    for canonical_id in body:
        canonical_id = canonical_id['canonical_id']
        req1 = requests.get('https://douban.fm/j/v2/song/' + canonical_id, header)
        song_body = json.loads(req1.text)
        song = {'canonical_id': canonical_id,
                'title': song_body['title'],
                'singers': [i['name'] for i in song_body['singers']]}
        print('已获得{}歌的数据'.format(song['title']))
        songs[canonical_id] = song
    return songs


cookies = '_ntes_nnid=969df69e3afb3f6e9f79c186a9a3a1b0,1524918342449; _ntes_nuid=969df69e3afb3f6e9f79c186a9a3a1b0; ' \
          '__f_=1526113550982; _iuqxldmzr_=32; WM_TID=R%2FJGexbkjJIlTaOOegRCrYzoV6k9KMDe; ' \
          '__utmz=94650624.1525080653.2.2.utmcsr=flybuxiu.com|utmccn=(referral)|utmcmd=referral|utmcct=/2340.html; ' \
          '__utmc=94650624; ' \
          'JSESSIONID-WYYY' \
          '=7Pkbsr2aRGwu0JIOn2D19ff3ztagJBKbN7vprNf89cge0KJS57GeEaeT2Ry1wI686A8Mc56a1oyPQFdzkcUNpNlxZZOuZU4d7lKpeAQc7H5Em8dg%2F9%2FMVUQ8r2%2FaF9hJnBOoA6ydsiQvKcm%2Fk%2FjaJkcYSFKAwbAEnVdlHw7hSISR2i8a%3A1530116519229; MUSIC_U=b387286bf9a7b993f13de34d5209520b23365ff388f755377bb32e7585eecad3a63a971d5df6ea2cf8643f0fed13ea5e54ee52482891d94f599d2aed53c216fd23deb182853baac2846c26372a8b4a41; __remember_me=true; __csrf=9513ed7d2908bb8d11737043fe8fb639; __utma=94650624.1021555160.1524918343.1530112979.1530115762.22; __utmb=94650624.1.10.1530115762 '
cookies = cookies.split(";")
cook = {}
for i in cookies:
    x = i.find("=")
    cook[i[:x]] = i[x + 1:]
# header['Cookie'] = cookies
driver.add_cookie(cook)