# coding:utf8
import pymongo

connection = pymongo.MongoClient('192.168.25.61', 28002)

try:

    cli = connection['DIR']
    for u in cli.col.find():
        print u
except Exception, e:
    print e

finally:
    print "connect"
