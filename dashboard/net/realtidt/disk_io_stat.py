# coding:utf8
"""
-------------------------------------------------
   File Name：     disk_io_stat.py
   Description :  读取硬盘IO状态
   Author :       tiankangbo
   date：         2017/3/13
-------------------------------------------------
   Change Activity:
-------------------------------------------------
"""
'''统计单位KB'''
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import psutil

def xint(list1):
    #将字符串转化为可以参加计算的整形数字
    v = list(map(lambda x: int(x), list1))
    return v

def disk_io_info():
    disk_if = []

    #获取硬盘读取写入数据量
    disk_r = psutil.disk_io_counters().read_bytes
    disk_w = psutil.disk_io_counters().write_bytes

    disk_read = disk_r / 1024
    disk_write = disk_w / 1024

    # 1.disk read speed kb/s
    #print disk_read
    disk_if.append(disk_read)
    # 2.disk write speed kb/s
    #print disk_write
    disk_if.append(disk_write)

    return xint(disk_if)


if __name__ == '__main__':
    print disk_io_info()
