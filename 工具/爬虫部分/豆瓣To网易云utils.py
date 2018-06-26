#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/6/25 0025 13:06
# @author  : zza
# @Email   : 740713651@qq.com

import json

import requests
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4882.400 QQBrowser/9.7.13059.400",
    "Cookie": 'bid=oVWkXcIFNU0; flag="ok"; dbcl2="52357979:CEk+opmv16U"; ck=NHNN; _gat=1; _ga=GA1.2.247535365.1514267287; _gid=GA1.2.141432331.1529901250'}

req1 = requests.get('https://douban.fm/j/v2/redheart/basic', headers=header)
body = json.loads(req1.text)['songs']
service_args = ['--ignore-ssl-errors=true',
                # '--proxy=119.41.168.186:53281', '--proxy-type=https',
                '--ssl-protocol=TLSv1']
dcap = dict(DesiredCapabilities.PHANTOMJS)
driver = webdriver.PhantomJS(executable_path="bin/phantomjs.exe", service_args=service_args,
                             desired_capabilities=dcap)


def 豆瓣获得所有歌():
    songs = {}
    for canonical_id in body:
        canonical_id = canonical_id['canonical_id']
        song = {}
        song['canonical_id'] = canonical_id
        req1 = requests.get('https://douban.fm/j/v2/song/' + canonical_id, header)
        song_body = json.loads(req1.text)
        song['title'] = song_body['title']
        song['singers'] = [i['name'] for i in song_body['singers']]
        print('已获得{}歌的数据'.format(song['title']))
        songs[canonical_id] = song
    return songs


