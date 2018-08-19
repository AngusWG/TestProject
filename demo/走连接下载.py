#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/8/5 15:08 
# @author  : zza
# @Email   : 740713651@qq.com



import requests
url ="https://vcdn01.findgaytube.com/video37/5/53/fc784b5d4b89193e84c9f5eb2ca91553.mp4?validfrom=1533451359&validto=1533453459&rate=812k&hash=itsINrB56tLIK5p2NCeCev%2BzqUI%3D"
proxies = {
    'http': 'http://127.0.0.1:9999',
    'https': 'http://127.0.0.1:9999',
}
resp = requests.get(url,
                    stream=True,
                    proxies=proxies,
                    timeout=60)
with open("a.mp4", 'wb') as fh:
    i = 0
    for chunk in resp.iter_content(chunk_size=1024):
        print(i)
        i += 1
        fh.write(chunk)
