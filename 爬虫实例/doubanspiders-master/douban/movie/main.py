#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/4/12 0012 15:26
# @author  : zza
# @Email   : 740713651@qq.com


if __name__ == '__main__':
    from scrapy import cmdline

    cmdline.execute('scrapy crawl movie'.split())