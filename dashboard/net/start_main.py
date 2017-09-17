# coding:utf8
"""
-------------------------------------------------
   File Name：     start_main.py
   Description :  工程启动函数
   Author :       tiankangbo
   date：         2017/3/13
-------------------------------------------------
   Change Activity:
-------------------------------------------------
"""
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import MySQLdb
import read_xml
import socket
import os

import multiprocessing

from datetime import datetime, timedelta
import time

time_interval = int(read_xml.get_val()[6])


def action(test):
    try:
        os.popen(test)
    except Exception, n:
        print "act ", n


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


def find_host_fun(conn_f):
    host_name = socket.gethostname()
    try:
        cursor = conn_f.cursor()
        cursor.execute("select * from nodes")
        list_nodes = list(cursor.fetchall())

        for i in range(len(list_nodes)):

            if host_name in list_nodes[i][1]:
                sql = "delete from nodes where nodename=" + "'" + host_name + "'"
                cursor.execute(sql)
                conn_f.commit()

            elif host_name not in list_nodes:
                pass

        cursor.close()
        conn_f.close()
    except Exception, s:
        print "find_host_fun ", s


def clear_mem():
    host_name1 = socket.gethostname()
    try:
        conn_c = conn_mysql()
        cursor = conn_c.cursor()

        sql = "select mem_stat from nodes where nodename=" + "'" + host_name1 + "'"
        sql1 = "update nodes set mem_stat=0 where nodename=" + "'" + host_name1 + "'"

        cursor.execute(sql)
        stat = cursor.fetchall()

        sta = stat[0][0]

        if 1 == int(sta):

            action('sync |echo 3 > /proc/sys/vm/drop_caches')

            cursor.execute(sql1)

            conn_c.commit()
            cursor.close()

        elif 0 == int(sta):

            #cursor.execute(sql)
            #print "stat==0重新检测", cursor.fetchall()
            cursor.close()
        conn_c.close()

    except Exception, f:
        print "clear_mem ", f


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


if __name__ == '__main__':

    conn = conn_mysql()

    try:
        find_host_fun(conn)

        qc = multiprocessing.Process(target=action, args=("python /dashboard/net/main.py", ))
        qa = multiprocessing.Process(target=compute, args=(clear_mem, 0, 0, 0, time_interval,))

        qc.start()
        time.sleep(5)

        qa.start()

        qa.join()
        qc.join()

    except Exception, a:
        print "start error", a
