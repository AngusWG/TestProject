#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/6/20 0020 11:02
# @author  : zza
# @Email   : 740713651@qq.com

# !/usr/bin/env python
# encoding: utf-8

"""
@author: wugang
@software: PyCharm
@file: prase_pdf.py
@time: 2017/3/3 0003 11:16
"""
import importlib
import sys

import requests
from tqdm import tqdm

importlib.reload(sys)

'''
 解析pdf 文本，保存到txt文件中
'''


def dd(url, filename):  # 传入url，以及下载文件的全路径filename
    # url = "http://www.jxepb.gov.cn/resource/uploadfile/file/20160307/20160307083510567.xls"
    response = requests.get(url, stream=True)
    # 用response储存在获取url的响应
    with open(filename, "wb") as handle:
        # 打开本地文件夹路径filename，以二进制写入，命名为handle
        for data in tqdm(response.iter_content()):
            # tqdm进度条的使用,for data in tqdm(iterable)
            handle.write(data)
    # 在handle对象中写入data数据


if __name__ == '__main__':
    dd("asd", "www....")
