# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HuxiuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field() # 标题
    link = scrapy.Field() # url
    posttime = scrapy.Field() # 发布时间
    author = scrapy.Field()
    nexttitle = scrapy.Field()
    instime = scrapy.Field()


