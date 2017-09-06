# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from __future__ import print_function
import scrapy
from scrapy.item import DictItem, Field


class HuxiuItem(scrapy.Item):
    #将字段列到列表里面，利用列表推倒式进行容器的创建
    field_list = ['title', 'link', 'posttime', 'author', 'nexttitle', 'instime']
    fields = {field_name: Field() for field_name in field_list}



