#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import time
import pytesseract
from PIL import Image
from bs4 import BeautifulSoup

def captcha(data):
    with open('captcha.jpg','wb') as fp:
        fp.write(data)
    time.sleep(1)
    image = Image.open("captcha.jpg")
    text = pytesseract.image_to_string(image)
    print( "机器识别后的验证码为：" + text)
    command = input("请输入Y表示同意使用，按其他键自行重新输入：")
    if (command == "Y" or command == "y"):
        return text
    else:
        return input('输入验证码：')

def zhihuLogin(username,password):

    # 构建一个保存Cookie值的session对象
    sessiona = requests.Session()
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}

    # 先获取页面信息，找到需要POST的数据（并且已记录当前页面的Cookie）
    html = sessiona.get('https://www.zhihu.com/#signin', headers=headers).content

    # 找到 name 属性值为 _xsrf 的input标签，取出value里的值
    _xsrf = BeautifulSoup(html ,'lxml').find('input', attrs={'name':'_xsrf'}).get('value')

    # 取出验证码，r后面的值是Unix时间戳,time.time()
    captcha_url = 'https://www.zhihu.com/captcha.gif?r=%d&type=login' % (time.time() * 1000)
    response = sessiona.get(captcha_url, headers = headers)


    data = {
        "_xsrf":_xsrf,
        "email":username,
        "password":password,
        "remember_me":True,
        "captcha": captcha(response.content)
    }

    response = sessiona.post('https://www.zhihu.com/login/email', data = data, headers=headers)
    print( response.text)

    response = sessiona.get('https://www.zhihu.com/people/maozhaojun/activities', headers=headers)
    print( response.text)


if __name__ == "__main__":
    #username = input("username")
    #password = input("password")
    zhihuLogin('xxxx@qq.com','ALAxxxxIME')