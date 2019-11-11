#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 下午6:58
# @Author  : zhaoyu
# @Site    : 
# @File    : test1.py
# @Software: PyCharm


import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]
    num = 1

    def parse(self, response):
        for quote in response.css('div.quote'):
            data = yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.xpath('span/small/text()').get(),
            }
            self.logger.debug('current num:{}'.format(self.num))
            self.logger.debug(data)
            self.num += 1

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)