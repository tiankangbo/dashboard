# coding:utf8
"""
-------------------------------------------------
   File Name：     cpu_stat.py
   Description :  读取CPU指标
   Author :       tiankangbo
   date：         2017/3/13
-------------------------------------------------
   Change Activity:
-------------------------------------------------
"""
'''统计单位`C'''

import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import os
import string
import psutil
import warn.sendmail
import warn.readjson
import nodes.node_info

def critical_value(temp):

    if int(temp[0]) > 90:
        #print "CPU压力预警"
        warn.sendmail.send_mail(warn.readjson.usage_command("cpu_stat1")+nodes.node_info.get_ip_in())
    elif int(temp[1]) > 75:
        #print "CPU温度预警"
        warn.sendmail.send_mail(warn.readjson.usage_command("cpu_stat2")+nodes.node_info.get_ip_in())
    else:
        pass

def get_temp():
    #获取温度和cpu使用率
    cpu_info = []
    temp = os.popen("sensors | egrep '(Core)'|awk '{print $3}' | cut -c2-5").read()
    get_temp = []
    for i in temp.split('\n'):
        if i == '':
            continue
        f = string.atof(i)
        get_temp.append(f)

    avg_temp = sum(get_temp) / len(get_temp)

    cpu_per = psutil.cpu_percent()
    cpu_info.append(cpu_per)
    #print avg_temp温度
    cpu_info.append(avg_temp)

    #print cpu_per CPU使用量
    critical_value(cpu_info)

    return cpu_info

if __name__ == '__main__':
    print get_temp()
