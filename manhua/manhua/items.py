# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ManhuaItem(scrapy.Item):
    # 目录名称
    title = scrapy.Field()
    # 图片链接
    url = scrapy.Field()
    # 图片名称
    imgname = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
