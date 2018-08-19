#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/8/19 15:01 
# @author  : zza
# @Email   : 740713651@qq.com
import os
import smtplib
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import redis
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap[
    "phantomjs.page.settings.userAgent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6716.400 QQBrowser/10.2.2214.40"
# dcap["phantomjs.page.settings.loadImages"] = True
browser = webdriver.PhantomJS(desired_capabilities=dcap)

r = redis.Redis(host='182.61.28.33', port=6379, db=0, password="123456")


def send_email():
    from_addr = "1169254037@qq.com"
    password = "vkyvmovizdsiigja"
    receivers = ['740713651@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header("菜鸟教程", 'utf-8')
    message['To'] = Header("测试", 'utf-8')
    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')

    msgAlternative = MIMEMultipart('alternative')
    message.attach(msgAlternative)

    # mail_msg = """
    # <p><img src="cid:image1"></p>
    # """
    # msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
    files2 = []
    files = os.listdir(".")
    for i in files:
        if i.endswith(".png"):
            files2.append(i)

    if len(files2) == 0:
        return
    for i in files2:
        # 指定图片为当前目录
        fp = open(i, 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()

        # 定义图片 ID，在 HTML 文本中引用
        mail_msg = """<p><img src="cid:{}"></p>""".format(i[:-4])
        msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
        msgImage.add_header('Content-ID', '<{}>'.format(i[:-4]))
        message.attach(msgImage)
        os.remove(i)
    ##############
    smtp_server = "smtp.qq.com"

    try:
        smtpObj = smtplib.SMTP_SSL(smtp_server, 465)  # SMTP协议默认端口是25
        smtpObj.login(from_addr, password)
        smtpObj.sendmail(from_addr, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


def main():
    id = 2036565412
    browser.get('https://weibo.com/u/{}?is_all=1'.format(id))
    browser.implicitly_wait(10)
    elements = browser.find_elements_by_xpath('//*[@class="WB_from S_txt2"]/a[1]')
    texts = list()
    for i in elements:
        url = i.get_attribute("href")
        url = url[:url.find("?")]
        texts.append(url)
        print(url)
    r.delete(id)
    for url in texts:
        c = r.hget(id, url)
        print(c)
        if c is None:
            browser.get(url)
            browser.implicitly_wait(30)
            while True:
                try:
                    browser.find_elements_by_xpath(
                        '//*[@node-type="feed_list_content"]')
                    break
                except:
                    continue
            file_name = "{}.png".format(url[url.rfind("/") + 1:])
            browser.save_screenshot(file_name)
            print(file_name, url)
            r.hset(id, url, True)


if __name__ == '__main__':
    main()
    send_email()
