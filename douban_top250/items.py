# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanTop250Item(scrapy.Item):
    # define the fields for your item here like:
    movie_name = scrapy.Field()
    # movie_img = scrapy.Field()
    # movie_detail_url = scrapy.Field()
    movie_ranting_num = scrapy.Field()
