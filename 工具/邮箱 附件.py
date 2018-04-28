#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/4/16 0016 9:49
# @author  : zza
# @Email   : 740713651@qq.com


# !/usr/bin/python3

import smtplib
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# 添加图片


def send_email():
    from_addr = "740713651@qq.com"
    password = "jmxlswooarwebceg"
    receivers = ['1169254037@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header("菜鸟教程", 'utf-8')
    message['To'] = Header("测试", 'utf-8')
    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')

    # 邮件正文内容
    # message.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))

    # file_name = 'test.txt'
    # 构造附件1，传送当前目录下的 test.txt 文件
    # att1 = MIMEText(open(file_name, 'rb').read(), 'base64', 'utf-8')
    # att1["Content-Type"] = 'application/octet-stream'
    # # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    # att1["Content-Disposition"] = 'attachment; filename="test.txt"'
    # message.attach(att1)

    msgAlternative = MIMEMultipart('alternative')
    message.attach(msgAlternative)

    mail_msg = """
    <p>Python 邮件发送测试...</p>
    <p><a href="http://www.w3cschool.cn">W3Cschool教程链接</a></p>
    <p>图片演示：</p>
    <p><img src="cid:image1"></p>
    """
    msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

    # 指定图片为当前目录
    fp = open('test.png', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    # 定义图片 ID，在 HTML 文本中引用
    msgImage.add_header('Content-ID', '<image1>')
    message.attach(msgImage)
    ##############
    smtp_server = "smtp.qq.com"

    try:
        smtpObj = smtplib.SMTP_SSL(smtp_server, 465)  # SMTP协议默认端口是25
        smtpObj.login(from_addr, password)
        smtpObj.sendmail(from_addr, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


if __name__ == '__main__':
    send_email()
