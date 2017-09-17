# coding:utf8
"""
-------------------------------------------------
   File Name：     message_info.py
   Description :  用来收集所有功能函数的返回值列表，并整理汇总好所有数据，等待主函数调用
   Author :       tiankangbo
   date：         2017/3/13
-------------------------------------------------
   Change Activity:
-------------------------------------------------
"""
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import os
import socket
import time
from datetime import datetime, timedelta

import nodes.node_info
import offlinetidt.disk_info, offlinetidt.Mem_info, offlinetidt.swap_info
import realtidt.cpu_stat, realtidt.disk_io_stat, realtidt.net_info

import read_xml

#从配置文件获取时间计算间隔
c_time = int(read_xml.get_val()[5])
#获取主机名
hostname = socket.gethostname()

def get_now_time():
    '''获取现在的时间'''
    ttime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    return ttime

def disk_io():
    '''获取硬盘读写数据量'''
    list_disk_io = []
    list_disk_io.extend(realtidt.disk_io_stat.disk_io_info())
    return list_disk_io

def net_io():
    '''流量进出量'''
    net_io = []
    net_io.extend(realtidt.net_info.net_info())
    return net_io

def fun_sub(list1, list1_1):
    '''计算列表差值，并生成新的列表'''
    v = list(map(lambda x, y:(x/c_time - y/c_time), list1, list1_1))
    return v

def compute(disk_io, day=0, hour=0, min=0, second=0):
    #定时器计算硬盘io速率和网络流量的上行下行速率
    list1 = disk_io()
    list2 = net_io()

    now = datetime.now()
    period = timedelta(days=day, hours=hour, minutes=min, seconds=second)
    next_time = now + period

    while True:
        
        time.sleep(second)
        # Get system current time
        iter_now = datetime.now()
        
        if (next_time-iter_now <= period):
            
            list1_1 = disk_io()
            list2_2 = net_io()
            #python协程,保存列表计算结果到生成器，此处，生成器默认元组类型
            yield fun_sub(list1_1, list1), fun_sub(list2_2, list2)

            next_time = iter_now + period
            continue

'''数据库dashboard的offlinetidt表数据'''
def fun_msg():
    #根据刷新时间不同，定义2个总信息列表, 初始化列表
    list_message = ['0']
    path1 = read_xml.get_val()[7]
    path2 = read_xml.get_val()[8]
    #扩展列表，汇总所有抓取的信息
    list_message.append(hostname)
    list_message.extend(offlinetidt.Mem_info.fun_memory())
    list_message.extend(offlinetidt.swap_info.fun_swap())
    list_message.extend(offlinetidt.disk_info.fun_disk(path1))

    if path2 is not None:
        list_message.extend(offlinetidt.disk_info.fun_disk(path2))
    else:
        list_message.extend(['0', '0', '0'])

    #now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    list_message.append(get_now_time())
    #协程yield
    yield list_message
    #print list_message
    # 间隔时间time_interval从配置文件读取

'''数据库dashboard的realtidt表数据'''
def fun_msg1():

    list_message1 = ['0']
    list_message1.append(hostname)
    #统计温度 and cpu使用率
    list_message1.extend(realtidt.cpu_stat.get_temp())

    p = compute(disk_io, day=0, hour=0, min=0, second=c_time)
    list11 = p.next()
    #将元组类型的元素添加到列表
    list_message1.append(list11[0][0])
    list_message1.append(list11[0][1])
    list_message1.append(list11[1][0])
    list_message1.append(list11[1][1])
    io_stat = os.popen("iostat -d -x | grep 'sda' | awk '{print $NF}'").read()
    list_message1.extend(io_stat.strip().split('\n'))

    list_message1.append(get_now_time())

    yield list_message1
    #print list_message1

'''数据库dashboard的nodes表数据'''
def fun_msg2():

    list_message2 = ['0']
    list_message2.append(hostname)
    list_message2.append(nodes.node_info.get_ip_in())
    list_message2.append('0')
    #now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    list_message2.append(get_now_time())
    #print list_message2
    yield list_message2

if __name__ == '__main__':
    #fun_msg()
    #print fun_msg1()
    fun_msg2()
