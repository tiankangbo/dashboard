# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.exceptions import DropItem
import pymongo
from scrapy.conf import settings
# class HuxiuPipeline(object):
#
#     def __init__(self):
#         self.file = open('huxiu.json', 'wb')
#
#
#     def process_item(self, item, spider):
#         if item['title']:
#             line = json.dumps(dict(item)) + "\n"
#             self.file.write(line)
#             return item
#         else:
#             raise DropItem("Missing title in %s " % item)

class HuxiuPipeline(object):

    def __init__(self):
        port = settings['MONGODB_PORT']
        host = settings['MONGODB_HOST']
        db_name = settings['MONGODB_DBNAME']
        client = pymongo.MongoClient(host=host, port=port)
        db = client[db_name]
        self.post = db[settings['MONGODB_DOCNAME']]

    def process_item(self, item, spider):
        book_info = dict(item)
        self.post.insert(book_info)
        return item
