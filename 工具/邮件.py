#!/usr/bin/env python
# coding:utf-8
"""
  Author:   shu--<httpservlet@yeah.net>
  Purpose: 日志模块
  Created: 2017/10/9
"""
import logging
import os
import smtplib
import socket
import sys
import threading
from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr, parseaddr
from logging.handlers import RotatingFileHandler
from smtplib import SMTPConnectError


class LoggerCommon(object):
    """ 创建日志对象 """

    def __init__(self, log_name='robot', logger_type='console', logfile=None, log_level=logging.DEBUG,
                 encoding='utf-8'):
        """
        @param log_name: 日志名称,相同的名称全局唯一对应一个Logger对象。缺省参数为root，返回默认Logger对象。
        @param logger_type: 日志风格
                - 输出到文件:file
                - 输出到系统标准输出:console
                - 上面两者都输出: all
        """
        if logger_type in ['all', 'file'] and not logfile:
            raise ValueError('Logfile cannot be empty. ')
        self.logger = logging.getLogger(log_name)
        self.logger.propagate = 0
        self.logger.setLevel(log_level)

        formatter = logging.Formatter("%(asctime)s [%(levelname)s]: %(message)s")

        if logger_type in ['all', 'file']:
            fh = RotatingFileHandler(logfile, mode='a', maxBytes=200 * 1024 * 1024, backupCount=1, encoding=encoding)
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)

        if logger_type in ['all', 'console']:
            ch = logging.StreamHandler()
            ch.setFormatter(formatter)
            self.logger.addHandler(ch)

    def debug(self, msg):
        if msg is not None:
            self.logger.debug(msg)

    def info(self, msg):
        if msg is not None:
            self.logger.info(msg)

    def warning(self, msg):
        if msg is not None:
            self.logger.warning(msg)

    def error(self, msg):
        if msg is not None:
            self.logger.error(msg)

    def critical(self, msg):
        if msg is not None:
            self.logger.critical(msg)

    @staticmethod
    def get_host_ip():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        finally:
            s.close()
        return ip

    @staticmethod
    def get_file_name():
        return os.path.realpath(sys.argv[0])

    @staticmethod
    def get_call_method_name():
        str_1 = ""
        # str_1 +=  sys._getframe().f_code.co_name + " \\ "
        if sys._getframe().f_back:
            str_1 += sys._getframe().f_back.f_code.co_name + " \\ "
            if sys._getframe().f_back.f_back:
                str_1 += sys._getframe().f_back.f_back.f_code.co_name + " \\ "
                if sys._getframe().f_back.f_back.f_back:
                    str_1 += sys._getframe().f_back.f_back.f_back.f_code.co_name + " \\ "
        str_1 += "\n _(:з」∠)_   \n "
        return str_1

    @staticmethod
    def get_host_name():
        return socket.getfqdn(socket.getfqdn())


class LoggerEmail(LoggerCommon):
    """把重要的日志内容通过邮件发送, 频率过高会封号一段时间"""

    # 基本不会改变的内容写入类属性
    # 主题 (默认主题不会去重, 也就是说出现几次会发几次邮件, 使用需谨慎)
    subject = 'GBI爬虫出现须主动处理的bug'
    # 收件人(可以多个收件人)
    receiver = {
        '740713651@qq.com': '邹镇安'
    }

    # 发件人及密码
    sender = {'robothetao@sina.com': 'GBI爬虫'}
    password = '123456987'
    smtp_server = 'smtp.sina.com'

    def __init__(self, *args, **kwargs):
        super(LoggerEmail, self).__init__(*args, **kwargs)
        if not (isinstance(LoggerEmail.receiver, dict) and isinstance(LoggerEmail.sender, dict)):
            self.error('receiver and sender must be dict')
            return

        self.formatted_sender_addr = self._format_addr(LoggerEmail.sender)
        self.formatted_receiver_addr = self._format_addr(LoggerEmail.receiver)
        # 发件人邮件地址
        self.sender_addr = self._format_addr(LoggerEmail.sender, True)
        # 收件人邮件地址  (str or list)
        self.receiver_addr = self._format_addr(LoggerEmail.receiver, True)
        # 已发送的主题, 不再发送
        self.sent_subject = set()
        self.tlock = threading.RLock()

        self.logger.send_email = self._send_email

    def _format_addr(self, s, only_addr=False):
        datas = []
        if only_addr:
            datas = list(s.keys())
        else:
            for k, v in s.items():
                name, addr = parseaddr('{} <{}>'.format(v, k))
                datas.append(formataddr((Header(name, 'utf-8').encode(), addr)))
            datas = ','.join(datas)

        if len(datas) == 1:
            return datas[0]
        else:
            return datas

    def __send_email(self, message, subject):
        self.debug('start send email...')
        try:
            self.tlock.acquire()
            import time
            time.sleep(10)
            # 当subject为空时可以重复发送
            if subject is not None:
                if subject in self.sent_subject:
                    # 不重复发送邮件
                    return None

                self.subject = subject

            msg = MIMEText(message, 'plain', 'utf-8')
            msg['From'] = self.formatted_sender_addr
            msg['to'] = self.formatted_receiver_addr
            msg['subject'] = Header(self.subject, 'utf-8').encode()

            server = smtplib.SMTP(self.smtp_server, 25)
            # 日志
            # server.set_debuglevel(1)
            server.login(self.sender_addr, self.password)
            server.sendmail(self.sender_addr, self.receiver_addr, msg.as_string())
            server.quit()
            self.sent_subject.add(self.subject)
            # 发送邮件并打印error日志
            self.error(message)
        except SMTPConnectError as err:
            self.error('connect failed we will retry, the reason is: {}'.format(err))
            return self.__send_email(message, subject=subject)
        except Exception as err:
            self.error('send_email failed: the reason is {}'.format(err))
            if subject in self.sent_subject:
                self.sent_subject.remove(subject)
        finally:
            self.tlock.release()

    def _send_email(self, message, subject=None):
        # 本地测试不发送邮件
        if LoggerCommon.get_host_ip().startswith('192.168'):
            return
        if message is None:
            return
        # 对文件进行加工:
        str = "\n"
        str += "*" * 60 + "\n"
        str += "\nhost_name : " + self.get_host_name()
        str += "\nhost_ip : " + self.get_host_ip()
        str += "\nfile_name : " + self.get_file_name()
        str += "\nmethod_name : " + self.get_call_method_name()
        str += "\n" + "*" * 60 + "\n"
        str += "\n" + message
        threading.Thread(target=self.__send_email, args=(str, subject)).start()


logger = LoggerEmail('robot', 'console', log_level=logging.DEBUG).logger

if __name__ == '__main__':
    logger.send_email('message')
    logger.send_email('测试', '测试')
