# coding:utf8
"""
-------------------------------------------------
   File Name：     Mem_info.py
   Description :  功能：统计内存的总空间，使用空间，剩余空间，统计单位MB
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
        #print "内存压力预警"
        warn.sendmail.send_mail(warn.readjson.usage_command("mem_out")+nodes.node_info.get_ip_in())
    else:
        pass

def fun_memory():
    list_Mem = []

    Mem = psutil.virtual_memory()
    Mem_total = Mem.total
    Mem_used = Mem.used
    Mem_free = Mem.free
    #Mem_percent = Mem.percent

    list_Mem.append(str(Mem_total/1024/1024))
    list_Mem.append(str(Mem_used/1024/1024))
    list_Mem.append(str(Mem_free/1024/1024))
    #list_Mem.append(str(Mem_percent)+'%')
    critical_value(Mem.percent)
    return list_Mem

if __name__ == '__main__':
    print "总大小---使用量---空余量------>使用百分比"
    print fun_memory()