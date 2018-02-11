# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class DoubanTop250Pipeline(object):
#     def process_item(self, item, spider):
#         return item
from collections import Counter


class JsonPipeline(object):
    index = 0

    def __init__(self):
        self.file = open('./result/top250.txt', 'wb')

    def process_item(self, item, spider):
        JsonPipeline.index += 1
        line = "{index}. {movie_name}, {movie_ranting_num} \n".format(index=JsonPipeline.index, **item)

        self.file.write(line.encode('utf-8'))
        return item
