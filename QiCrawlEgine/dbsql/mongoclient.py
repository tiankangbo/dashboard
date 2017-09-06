#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pymongo import MongoClient

settings = {
    "ip":'127.0.0.1',
    "port":27017,
    "db_name" : "mydb",
    "set_name" : "test_set"
}

class MyMongoDB(object):
    def __init__(self, input):
        try:
            self.conn = MongoClient(settings["ip"], settings["port"])
            self.dic = input
        except Exception as e:
            print(e)
        self.db = self.conn[settings["db_name"]]
        self.my_set = self.db[settings["set_name"]]

    def insert(self):
        self.my_set.insert(self.dic)

    # def update(self, newdic):
    #     self.my_set.update(self.dic, newdic)

    def delete(self):
        self.my_set.remove(self.dic)

    def dbfind(self):
        data = self.my_set.find(self.dic)
        for result in data:
            print(result["name"],result["age"])


def main():
    dic={"name":"zhangsan","age":18}
    mongo = MyMongoDB(dic)
    mongo.insert()
    mongo.dbfind()

    # mongo.update({"$set":{"age":"25"}})
    # mongo.dbfind()

    # mongo.delete()
    # mongo.dbfind()

if __name__ == "__main__":
    main()