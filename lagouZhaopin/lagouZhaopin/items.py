# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouzhaopinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    company = scrapy.Field()    #招聘方
    jobname = scrapy.Field()    #职位名称
    salary = scrapy.Field()     #薪资待遇
    aboutperson = scrapy.Field()    #人员素质要求
    jobdesc = scrapy.Field()    #工作描述
    address = scrapy.Field()    #公司地址
    aboutcompany = scrapy.Field()   #公司概况
    posttime = scrapy.Field()   #发布时间
    instime = scrapy.Field()    #抓取时间

