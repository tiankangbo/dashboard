# coding:utf8
"""
-------------------------------------------------
   File Name：     main.py
   Description :  工程main文件，执行数据入库操作
   Author :       tiankangbo
   date：         2017/3/13
-------------------------------------------------
   Change Activity:
-------------------------------------------------
"""

import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import multiprocessing
import sys

import MySQLdb
import message_info
import read_xml

from datetime import datetime, timedelta
import time


def create_conn():

        conn = mes_mysql()
        if conn is None:
            conn = mes_mysql()
        else:
            conn.ping(True)
        return conn


def mes_mysql():
        conn = MySQLdb.connect(
                host=read_xml.get_val()[0],
                port=int(read_xml.get_val()[1]),
                user=read_xml.get_val()[2],
                passwd=read_xml.get_val()[3],
                db=read_xml.get_val()[4],
                charset='utf8'
        )
        return conn


def insert_fun():

        try:
                conn = create_conn()
                q = message_info.fun_msg2()
                list_message3 = q.next()
                cursor = conn.cursor()

                cursor.execute(
                        'insert into nodes(id, nodename, ip, mem_stat, insert_time) values (%s, %s, %s, %s, %s)',
                        list_message3)

                conn.commit()
                cursor.close()
                conn.close()

        except Exception, e:
                #cursor.rollback()
                #cursor.close()
                print "nodes : ", e

def insert_fun1():

        while True:
                try:
                        conn = create_conn()
                        l = message_info.fun_msg1()
                        list_message2 = l.next()

                        cursor = conn.cursor()
                        cursor.execute('insert into realtidt(id, nodename, cpu_usage, cpu_temp, net_up, net_down, disk_rs, disk_ws, disk_io, insert_time)'
                                       ' values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', list_message2)
                        conn.commit()
                        cursor.close()
                        conn.close()

                except Exception, e:
                        print "realtidt : ", e


def insert_fun2():

        try:
                conn = create_conn()
                p = message_info.fun_msg()
                list_message = p.next()

                cursor = conn.cursor()
                cursor.execute(
                        'insert into offlinetidt(id, nodename, mem_total, mem_used, mem_free, swap_total, swap_used, swap_free, disk_total, disk_used, disk_free, disk1_total, disk1_used, disk1_free, insert_time) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                        list_message)

                conn.commit()
                cursor.close()
                conn.close()

        except Exception, e:
                print "offlinetidt : ", e

def compute(fun, day=0, hour=0, min=0, second=0):
    
    fun()
    now = datetime.now()
    period = timedelta(days=day, hours=hour, minutes=min, seconds=second)
    next_time = now + period

    while True:

        time.sleep(second)
        iter_now = datetime.now()

        if (next_time-iter_now<=period):
            fun()
            next_time = iter_now+period
            continue

def main():

        try:
                time_interval1 = int(read_xml.get_val()[6])
                # mysql->table, dashboard.nodes
                insert_fun()
                #mysql->table, dashboard.realtidt
                pp = multiprocessing.Process(target=insert_fun1, args=())
                #mysql-table, dashboard.offlinetidt
                qq = multiprocessing.Process(target=compute, args=(insert_fun2, 0, 0, 0, time_interval1,))

                #yy.start()
                pp.start()
                qq.start()

                #yy.join()
                pp.join()
                qq.join()

        except MySQLdb.Error, msg:
                print "error , conn has gone away", msg
                sys.exit(1)

if __name__ == '__main__':

        main()
