#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @author: x.huang
# @date:18-2-11
from scrapy.selector import HtmlXPathSelector
from scrapy.spiders import Spider

from douban_top250.items import DoubanTop250Item


class Top250Spider(Spider):
    name = 'douban-top250'

    @property
    def start_urls(self):

        start_url_list = []
        for i in range(0, 250, 25):
            start_url_list.append('https://movie.douban.com/top250?start={}'.format(i))
        return start_url_list

    def parse(self, response):
        current_url = response.url  # 爬取时请求的url
        body = response.text  # 返回的html
        unicode_body = response.body_as_unicode()  # 返回的html unicode编码
        hxs = HtmlXPathSelector(response)

        for i in range(1, 26):
            item = DoubanTop250Item()
            item['movie_name'] = hxs.select(
                '//li[{}]/div[@class="item"]//div[@class="info"]//span[1]/text()'.format(i)).extract_first()
            item['movie_ranting_num'] = hxs.select(
                '//li[{}]//span[@class="rating_num"]/text()'.format(i)).extract_first()
            yield item
