
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouzpItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city = scrapy.Field()
    company_name = scrapy.Field()
    size = scrapy.Field()
    edu = scrapy.Field()
    financeStage = scrapy.Field()
    firstType = scrapy.Field()
    industryField = scrapy.Field()
    name = scrapy.Field()
    salary = scrapy.Field()
    secondType = scrapy.Field()
    workYear = scrapy.Field()
    time = scrapy.Field()
