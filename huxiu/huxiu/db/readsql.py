# coding:utf8
__author__ = 'tiankangbo'
"""
本文件的主要任务是读取数据库里的代理ip
"""

import sqlite3

conn = sqlite3.connect('proxy.db')
print("sqlite connect is success")
c = conn.cursor()

cursor = c.execute("SELECT id, ip, port, types, protocol, country, area, updatetime, speed, score  from proxys")

with open("ipproxy.txt", 'wb') as f:

    for row in cursor:
        # print(row[0])
        print(row[1], row[2])
        print(row[4], type(row[4]))
        if row[4] == int(0):
            f.write("http://"+row[1]+":"+row[2])
        # else:
        #     f.write("https://" + row[1] + ":" + row[2])
        # print()
        # print(row[3])
        # print(row[4])
        # print(row[5])
        # print(row[6])
        # print(row[7])
        # print(row[8])
        # print(row[9])
f.close()
conn.close()
