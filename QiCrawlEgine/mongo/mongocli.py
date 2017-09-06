#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from pymongo import MongoClient

settings = {
    "ip":'127.0.0.1',
    "port":27017,
    # "db_name" : "mydb",
    # "set_name" : "test_set"
}

class MyMongoDB(object):
    def __init__(self, mydb, myset):

        try:
            self.conn = MongoClient(settings["ip"], settings["port"])
        except Exception as e:
            print(e)
        # self.db = self.conn[settings["db_name"]]
        # self.my_set = self.db[settings["set_name"]]
        self.db = self.conn[mydb]
        self.my_set = self.db[myset]

    def insert(self, dic):
        self.my_set.insert(dic)

    def update(self, dic, newdic):
        self.my_set.update(dic, newdic)

    def delete(self, dic):
        self.my_set.remove(dic)

    def dbfind(self, dic):
        return self.my_set.find(dic)


if __name__ == '__main__':
    dic={"name":"zhangsan","age":18}
    mongo = MyMongoDB("mydb", "myset")
    mongo.insert(dic)
    for data in mongo.dbfind({"name":"zhangsan"}):
        print(data)

    # mongo.update({"$set":{"age":"25"}})
    # mongo.dbfind()

    # mongo.delete({"name":"zhangsan"})