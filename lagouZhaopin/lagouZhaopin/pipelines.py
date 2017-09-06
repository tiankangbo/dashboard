# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings

class LagouzhaopinPipeline(object):

    def __int__(self):
        port = settings('MONGODB_PORT')
        host = settings('MONGODB_HOST')
        dbname = settings('MONGODB_DBNAME')
        client = pymongo.MongoClient(host=host, port=port)
        db = client[dbname]
        self.post = db[settings('MONGODB_DOCNAME')]

    def process_item(self, item, spider):
        lago = dict(item)
        self.post.insert(lago)
        return item
