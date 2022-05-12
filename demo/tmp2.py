#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2021/9/15 10:54
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : tmp.py
import tq


from importlib import reload 
reload(tq)

import  paramiko
def get_dir_list():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("192.168.0.122", username="root", password="lksense@2018")
    ftp = ssh.open_sftp()
    ftp.listdir("/opt/software/")
%time get_dir_list()
# Wall time: 213 ms
%timeit get_dir_list()
# 195 ms ± 10.2 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)