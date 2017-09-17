# coding:utf8
"""
-------------------------------------------------
   File Name：     disk_info.py
   Description :  功能：统计硬盘的总空间，使用空间，剩余空间，统计单位MB
   Author :       tiankangbo
   date：         2017/3/13
-------------------------------------------------
   Change Activity:
-------------------------------------------------
"""
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import warn.sendmail
import warn.readjson
import nodes.node_info
import psutil

def critical_value(temp):

    if int(temp) > 85:
        #print "磁盘不足预警"
        warn.sendmail.send_mail(warn.readjson.usage_command("disk_out")+nodes.node_info.get_ip_in())
    else:
        pass

def fun_disk(path):
    #统计硬盘信息的大列表
    list_disk = []

    disk_message = psutil.disk_usage(path)
    disk_total = disk_message.total
    disk_used = disk_message.used
    disk_free = disk_message.free
    #disk_percent = disk_message.percent

    list_disk.append(str(disk_total/1024/1024))
    list_disk.append(str(disk_used/1024/1024))
    list_disk.append(str(disk_free/1024/1024))
    #list_disk.append(str(disk_percent)+'%')
    #将列表信息，返回给主程序
    #print list_disk
    critical_value(disk_message.percent)
    return list_disk

if __name__ == '__main__':
    print "总大小---使用量---空余量------>使用百分比"
    print fun_disk("/root")
