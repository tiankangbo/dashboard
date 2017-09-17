# coding:utf8
"""
-------------------------------------------------
   File Name：     clear_Sql.py
   Description :  清理数据库旧数据
   Author :       tiankangbo
   date：         2017/3/13
-------------------------------------------------
   Change Activity:
-------------------------------------------------
"""

import MySQLdb
import read_xml
import socket
import os
import time
import multiprocessing

from datetime import datetime, timedelta

time_interval = int(read_xml.get_val()[5])



def compute(fun, day=0, hour=0, min=0, second=0):

    fun()
    now = datetime.now()
    period = timedelta(days=day, hours=hour, minutes=min, seconds=second)
    next_time = now + period

    while True:

        time.sleep(day*24*60*60)
        iter_now = datetime.now()

        if (next_time-iter_now<=period):
            fun()
            next_time = iter_now+period
            continue


def mes_mysql():
    conn_m = MySQLdb.connect(
        host=read_xml.get_val()[0],
        port=int(read_xml.get_val()[1]),
        user=read_xml.get_val()[2],
        passwd=read_xml.get_val()[3],
        db=read_xml.get_val()[4],
        charset='utf8'
    )
    return conn_m


def conn_mysql():
    conn_m = mes_mysql()
    if conn_m is None:
        conn_m = mes_mysql()
    else:
        conn_m.ping(True)
    return conn_m



def del_sql():

    sql1 = "truncate table realtidt"
    sql2 = "truncate table offlinetidt"
    try:

        conn1 = conn_mysql()
        conn2 = conn_mysql()

        cursor1 = conn1.cursor()
        cursor2 = conn2.cursor()

        cursor1.execute(sql1)
        cursor2.execute(sql2)

        conn1.commit()
        conn2.commit()

        cursor1.close()
        cursor2.close()

        conn1.close()
        conn2.close()
    except:
        pass

if __name__ == '__main__':

    conn = conn_mysql()

    try:
        qb = multiprocessing.Process(target=compute, args=(del_sql, time_interval, 0, 0, 0,))

        qb.start()

        qb.join()

    except Exception, a:
        print "start error", a
