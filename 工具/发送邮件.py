#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2019/3/22 11:24
# @Author  : zza
# @Email   : 740713651@qq.com
import yagmail

# 连接邮箱服务器
yag = yagmail.SMTP(user="lijianzhaoyou@163.com", password="填自己的", host='smtp.163.com')

# 邮箱正文
contents = ['今天是周末,我要学习, 学习使我快乐;', '<a href="https://www.python.org/">python官网的超链接</a>', './girl.jpg']

# 发送邮件
yag.send('zhaoolee@gmail.com', '主题:学习使我快乐', contents)