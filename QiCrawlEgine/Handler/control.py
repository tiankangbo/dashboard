# coding:utf8
"""
-------------------------------------------------
   File Name：     control.py
   Description :  爬虫启动暂停控制操作
   Author :       tiankangbo
   date：         2017/9/25
-------------------------------------------------
   Change Activity:
-------------------------------------------------
"""
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import os
import signal
import subprocess
import logging

from multiprocessing import Process
from Handler.dbClient import MyMongoDB
from Handler import listDir
from Config.settings import template_settings
# from Spiders import mayi


class schedulerQi(Process):
    '''
    schedulerQi类: 开启调度爬虫任务类
    '''

    def __init__(self, template, username, jobname, keyword, date_in):
        '''
        :param template: 采用爬虫的类模板
        :param username: 用户名
        :param jobname: 任务名
        :param keyword: 关键字
        '''
        Process.__init__(self)
        self.template_ = template
        self.user_ = username
        self.keyword_ = keyword
        self.jobname_ = jobname
        self.date_in_ = date_in

        try:
            if self.jobname_ is not None:
                self.set_name = self.jobname_
            else:
                self.set_name = self.template_
        except:
            '''此处属于测试'''
            raise NameError

    def run(self):
        '''
        :return: 函数功能 -> 启动相对应实例化的爬虫类程序, 并将爬虫获取的数据进行存储
                 要求所有的爬虫类数据调用出口函数,命名规则一致,命名为: run()
        '''

        try:
            for name in listDir.listDir('../Spiders'):
                exec("from Spiders import " + name)
        except Exception as e:
            raise ImportError

        dynamic_ = eval(template_settings[self.template_] + '()')  # 实例化爬虫类
        dic = dynamic_.run(self.keyword_)  # 启动爬虫类
        self.dropOldset_(my_db=self.user_, dic_set=self.set_name)  # 清理旧的数据集合,避免任务爬取数据重复

        try:
            store = MyMongoDB(mydb=self.user_, myset=self.set_name)
            while dic.__next__:
                store.insert(next(dic))

        except Exception as e:
            logging.info(e)

    def dropOldset_(self, my_db, dic_set):
        '''
        :param my_db: 数据库名
        :param dic_set: 集合名字
        :return: 函数功能 -> 数据插入mongo之前, 先把旧的已经被导出的旧数据删除, 数据库不为用户提供太多的临时存储空间.
        '''
        try:
            user_db = MyMongoDB(mydb=my_db, myset=dic_set)
            if dic_set in user_db.getset():
                user_db.drop(dic_set)

        except Exception as e:
            mes = e, 'dropOldset failed!'
            logging.info(mes)


class stopProcess(object):
    '''
    stopProcess类: 中断爬虫功能类
    '''

    def __init__(self, pid):
        ''':param pid: 爬虫的真实进程,利用该进程号对爬虫进行信息化控制'''
        self.thispid = pid

    def isLive_(self):
        ''':return: 判断进程是否是live状态'''
        return subprocess.call('ps -p ' + str(self.thispid), shell=True)

    def stop_(self):
        if 0 == self.isLive_():
            try:
                os.kill(int(self.thispid), signal.SIGINT)
                # os.kill(int(self.thispid), signal.pause())
            except OSError as e:
                logging.info(e)
        else:
            logging.info(self.thispid, "......is not running")

    def kill_(self):
        if 0 == self.isLive_():
            os.kill(int(self.thispid), signal.SIGKILL)
        else:
            logging.info("......process is not killed")


if __name__ == '__main__':
    a = schedulerQi('huxiu')
    a.start()
    a.join()
