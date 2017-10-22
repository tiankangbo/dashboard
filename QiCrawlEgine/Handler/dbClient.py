# coding:utf8
"""
-------------------------------------------------
   File Name：     dbClient.py
   Description :  数据库操作文件
   Author :       tiankangbo
   date：         2017/9/25
-------------------------------------------------
   Change Activity:
-------------------------------------------------
"""
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import logging

from pymysql import connect
from pymongo import MongoClient
from Config.settings import db_settings


class MyMongoDB(object):
    '''
    MyMongoDB类: mongodb数据库操作类
    '''
    def __init__(self, mydb, myset):
        '''
        Description: 封装数据库操作类,预留增删查改接口
        :param mydb: 数据库名
        :param myset: 集合名字
        '''
        try:
            self.conn_ = MongoClient(db_settings["mongodb_ip"], db_settings["mongodb_port"])
        except Exception as e:
            mes = e, 'mongo client (self.conn_) error!'
            logging.info(mes)
        self.db_ = self.conn_[mydb]
        self.my_set = self.db_[myset]

    def insert(self, dic):
        self.my_set.insert(dic)

    def update(self, dic, newdic):
        self.my_set.update(dic, newdic)

    def delete(self, dic):
        self.my_set.remove(dic)

    def drop(self, my_set):
        '''
        每次任务的执行, 爬虫所获取的数据, 对应唯一的数据库->集合, 当任务被同一个用户执行多次时候, 旧的数据集合将被清理掉.
        '''
        try:
            self.db_.drop_collection(my_set)
        except Exception as e:
            mes = e, '清理旧数据集失败'
            logging.info(mes)

    def getset(self):
        '''
        获取该数据库中所有集合set
        '''
        return self.db_.collection_names(include_system_collections=False)

    def dbfind(self, dic):
        return self.my_set.find(dic)

    def select(self):
        pass


class MysqlDB(object):
    '''
    MysqlDB类: Mysql数据库操作类
    '''

    def __init__(self):
        '''
        Description: 封装Mysql数据库操作类,预留增删查改接口, 主要用来更改任务表数据库
        '''
        self.host_ = db_settings['mysql_ip']
        self.user_ = db_settings['mysql_user']
        self.pwd_ = db_settings['mysql_passwd']
        self.dbname_ = db_settings['mysql_db']

    def getcursor_(self):
        '''获取数据库操作游标'''
        try:
            self.db_ = connect(self.host_, self.user_, self.pwd_, self.dbname_, charset='utf8')
        except Exception as e:
            mes = e, 'mysql connect (self.db_) error!'
            logging.info(mes)
        cur_ = self.db_.cursor()
        return cur_

    def select_(self, sql):
        this_cur = self.getcursor_()
        this_cur.execute(sql)
        rows = this_cur.rowcount
        dataTuple = this_cur.fetchall()
        this_cur.close()
        self.db_.close()
        return dataTuple, rows

    def delete_(self, sql):
        this_cur = self.getcursor_()
        try:
            this_cur.execute(sql)
            self.db_.commit()
        except Exception as e:
            logging.info(e)
            self.db_.rollback()
        this_cur.close()
        self.db_.close()

    def update_(self, sql):
        this_cur = self.getcursor_()
        try:
            this_cur.execute(sql)
            self.db_.commit()
        except Exception as e:
            logging.info(e)
            self.db_.rollback()
        this_cur.close()
        self.db_.close()

    def insert_(self, sql):
        this_cur = self.getcursor_()
        try:
            this_cur.execute(sql)
            self.db_.commit()
        except Exception as e:
            logging.info(e)
            self.db_.rollback()
        this_cur.close()
        self.db_.close()


if __name__ == '__main__':
    # dic = {"name": "zhangsan", "age": 18}
    mongo = MyMongoDB("xiaohong", "huxiu")
    # mongo.insert(dic)
    for data in mongo.dbfind():
        print(data)
        # print(mongo.getset())

        # if "myset" in mongo.getset():
        #     print("yes")
        # else:
        #     print("no")

        # mongo.drop()
        # sql = 'update spiderinfo set Jobid=' + '1234'
        # a = MysqlDB()
        # print(a.select_('select * from spiderinfo'))
        # a.update_(sql)
        # print(a.select_('select * from spiderinfo'))
