# coding:utf8
"""
-------------------------------------------------
   File Name：     main.py
   Description :  启动引擎文件
   Author :       tiankangbo
   date：         2017/10/12
-------------------------------------------------
   Change Activity:
-------------------------------------------------
"""
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import os
import multiprocessing
from Handler import autoSql
from Config import settings

HOST = settings.db_settings['mysql_ip']
PORT = settings.db_settings['mysql_port']
USER = settings.db_settings['mysql_user']
PASSWD = settings.db_settings['mysql_passwd']

path1 = '../Handler/'
filename1 = 'miniMonitor.py'
path2 = '../Api/'
filename2 = 'runQicrawlEgine.py'
path3 = '../Config/QicrawlDB.sql'
DB = 'QicrawlDB'


def createSQL():
    '''自动检测创建mysql数据库,导入表结构'''
    autoSql.autoDB.autoDB_(HOST=HOST, USER=USER, PASSWD=PASSWD, DB=DB, FILEPATH=path3)


def takeProcess(path, filename):
    '''脚本执行'''
    return os.popen('python3 ' + path + filename)


def ping():
    '''测试网络环境'''
    import subprocess

    try:
        return subprocess.call('ping -c 5 -w 5 www.baidu.com', stdout=open('/dev/null', 'w'), stderr=subprocess.STDOUT,
                               shell=True)

    except Exception as e:
        print(e)


def startProcess():
    print('***   welcome to qicrawlEgine   ***')

    print('* init mysql...')
    createSQL()
    print('init mysql done !')

    print('* test network...')
    pingtest = ping()
    print(pingtest, type(pingtest))

    if 0 == pingtest:
        print('internet connections !')

        try:
            tpro = multiprocessing.Process(target=takeProcess, args=(path1, filename1))
            mpro = multiprocessing.Process(target=takeProcess, args=(path2, filename2))

            tpro.start()
            print('开启引擎成功 !')
            mpro.start()
            print('开启mini监控成功 !')

            tpro.join()
            mpro.join()

        except Exception as e:
            print('启动错误 !', e)

    else:
        print('无网状态, 请检查网络服务 !')


if __name__ == '__main__':
    startProcess()