# coding:utf8
__author__ = 'tiankangbo'

import pymongo

try:
    client = pymongo.MongoClient('localhost', 27017)
    db = client.pythonSpider
    collection = db.pythonSpider

    for mes in collection.find():
        print mes

except Exception, e:
    print e
