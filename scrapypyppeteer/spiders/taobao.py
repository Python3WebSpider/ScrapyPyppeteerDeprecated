# -*- coding: utf-8 -*-
from scrapy import Spider, Request


class TaobaoSpider(Spider):
    name = 'taobao'
    allowed_domains = ['s.taobao.com']
    start_url = 'http://s.taobao.com/search?q={keyword}'
    keywords = ['ipad']
    
    def start_requests(self):
        for keyword in self.keywords:
            url = self.start_url.format(keyword=keyword)
            print(url)
            yield Request(url, callback=self.parse_list)
    
    def parse_list(self, response):
        with open('taobao.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
