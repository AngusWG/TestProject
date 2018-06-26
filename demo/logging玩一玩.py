#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/6/26 0026 16:59
# @author  : zza
# @Email   : 740713651@qq.com
import logging
from logging.handlers import RotatingFileHandler

formatter = logging.Formatter(
    "-----> [%(asctime)s] [%(levelname)s] [%(filename)s<%(lineno)d>-%(module)s.%(funcName)s]: %(message)s")
logging.basicConfig(
    level=logging.INFO,
    format="---> [%(filename)s] %(funcName)s: %(message)s",
    # datefmt='%Y-%m-%d %H:%M:%S',
    # filename='crawler_info.log',
    # filemode='a'
)
# 定义RotatingFileHandler, 最多备份5个日志, 每个日志最大10M
info_handler = RotatingFileHandler('crawler_info1.log', mode='a', maxBytes=1024 * 1024 * 512, backupCount=5,
                                   encoding='utf-8')
info_handler.setLevel(logging.INFO)
info_handler.setFormatter(formatter)
logging.getLogger('').addHandler(info_handler)

error_handler = RotatingFileHandler('crawler_error.log', mode='a', maxBytes=1024 * 1024 * 512, backupCount=5,
                                    encoding='utf-8')
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)
logging.getLogger('').addHandler(error_handler)
log = logging

log.info(123)
log.debug(123)
