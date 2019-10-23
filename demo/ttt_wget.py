#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2019/9/11 18:19
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : ttt_wget.py

import wget, tarfile
import os

# 网络地址
DATA_URL = 'http://www.robots.ox.ac.uk/~ankush/data.tar.gz'
# 本地硬盘文件
# DATA_URL = '/home/xxx/book/data.tar.gz'

out_f_name = 'abc.tar.gz'

wget.download(DATA_URL, out=out_f_name)
# 提取压缩包
tar = tarfile.open(out_f_name)
tar.extractall()
tar.close()
# 删除下载文件
os.remove(out_f_name)
