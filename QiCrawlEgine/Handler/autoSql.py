# coding:utf8
"""
-------------------------------------------------
   File Name：     autoSql.py
   Description :  自动创建mysql数据库文件
   Author :       tiankangbo
   date：         2017/10/17
-------------------------------------------------
   Change Activity: 1,实际自动化部署文件
                    2,修复了当数据库已存在时, 空表结构原表BUG
-------------------------------------------------
"""
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import re
from pymysql import connect
from subprocess import Popen


class autoDB(object):
    def __init__(self):
        pass

    @staticmethod
    def autoDB_(HOST, USER, PASSWD, DB, FILEPATH):
        # 主机IP, mysql用户, mysql用户密码, 数据库名, sql文件路径
        try:
            host = HOST
            user = USER
            passwd = PASSWD
            db = DB
            file = FILEPATH

            sql_showtables = 'SHOW TABLES;'
            sql_useDB = 'USE ' + DB

            conn = connect(host, user, passwd, charset='utf8')

            cur = conn.cursor()
            cur.execute('create database IF NOT EXISTS ' + db)

            cur.execute(sql_useDB)
            cur.execute(sql_showtables)
            # 列出数据库中所有的表
            table_list = [re.sub("'", '', each) for each in re.findall('(\'.*?\')', str([cur.fetchall()]))]

            if table_list:
                pass
            else:
                '''存在逻辑bug, 如果数据库已经存在,仍然会导入空的表结构,覆盖现有的table, 解决中...'''

                def impSQL():
                    try:
                        fp = open(os.devnull, 'w')
                        text = "mysql -u%s -p'%s' %s < %s" % (user, passwd, db, file)
                        process = Popen(text, stdout=fp, stderr=fp, shell=True)
                        process.communicate()
                        fp.close()

                    except Exception as e:
                        raise e

                return impSQL()

            cur.close()
            conn.close()

        except Exception as e:
            raise e


if __name__ == '__main__':
    # 主机IP, mysql用户, mysql用户密码, mysql数据库名, sql文件路径
    autoDB.autoDB_('127.0.0.1', 'root', 'pa$$w0rd', 'QicrawlDB', '../Config/QicrawlDB.sql')
