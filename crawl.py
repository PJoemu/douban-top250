#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @author: x.huang
# @date:18-2-11
from scrapy import cmdline

if __name__ == '__main__':
    cmdline.execute('scrapy crawl douban-top250'.split())
