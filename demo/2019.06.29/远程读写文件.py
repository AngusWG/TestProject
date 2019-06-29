#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2019/5/6 14:46
# @Author  : zza
# @Email   : 740713651@qq.com
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.1.1', username='root', password='123456')

ftp = ssh.open_sftp()
ftp.listdir("/home/zza")
a = ftp.file("/home/zza/hdf5.py", "r").read()
# filea = ftp.get('/var/www/folder_image/', '#')
# Here coded how we open the dir and read one by one all images property(name,size,path,etc.)
ftp.close()
