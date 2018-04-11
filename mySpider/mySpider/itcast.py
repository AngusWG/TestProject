# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['http://www.itcast.cn/channel/teacher.shtml']
    start_urls = ['http://itcast.cn/']

    def parse(self, response):
        filename = "teacher.html"
        open(filename, 'w').write(response.body)