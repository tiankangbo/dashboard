# coding:utf8
"""
-------------------------------------------------
   File Name：     net_info.py
   Description :  读取网络上行下行速度
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

def net_info():
    #获取网络接收和发送量
    net_if = []

    s = psutil.net_io_counters().bytes_sent
    r = psutil.net_io_counters().bytes_recv

    net_sent = s/1024
    net_recv = r/1024

    # net sent speed kb/s
    #print net_sent
    net_if.append(net_sent)
    # net reveive speed kb/s
    #print net_recv
    net_if.append(net_recv)

    return xint(net_if)

if __name__ == '__main__':
    print net_info()
