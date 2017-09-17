# coding:utf8
"""
-------------------------------------------------
   File Name：     node_info.py
   Description :  读取内网卡IP
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
import re

def get_ip_out():
    #get ip enable connect 8.8.8.8
    ip_list = []
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.connect(('8.8.8.8', 80))
        IP = sock.getsockname()[0]
        ip_list.append(IP)
    except Exception, e:
        print "None ip out", e
    finally:
        ip_list.append('127.0.0.1')
        sock.close()
    return set(ip_list)

def find_ip(list_ip):
    #import re to find ip
    l = []
    for i in list_ip:
        if re.search('(\d){1,3}(\.\d+){3}', i):
            l.append(re.search('(\d){1,3}(\.\d+){3}', i).group())
        else:
            pass
    return sorted(l)

def list_all_ip():
    #get all ip
    list_all = []
    ip = os.popen("ifconfig | awk '/inet/{print$2}' | awk -F : '{print$2}'").read()
    list_all.extend(ip.strip().split('\n'))
    return set(find_ip(list_all))

def get_set(get_ip):
    #sorted ip(all ip sorted)
    lists = []
    for i in get_ip:
        lists.append(i)
    lt = sorted(lists)
    return lt[1]

def get_ip_in():
    #get ip in area network
    if len(list_all_ip()) <= 1:
        list_in = ['0']
        return list_in
    if len(list_all_ip()) == 2:
        return get_set(list_all_ip())
    else:
        #use ^ to get
        list = get_ip_out() ^ list_all_ip()
        #get list[1]
        return get_set(list)

if __name__ == '__main__':
    print get_ip_in()

