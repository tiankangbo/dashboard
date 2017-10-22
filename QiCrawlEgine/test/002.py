# coding:utf8

import socket
import fcntl
import struct
import psutil


# 获取IP地址
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(
        fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', bytes(ifname[:15], encoding='utf8')))[20:24])


# 获取mac地址
def get_mac_addr(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927, struct.pack('256s', bytes(ifname[:15], encoding='utf-8')))
    return ''.join(['%02x:' % b for b in info[18:24]])[:-1]


# ip和mac
def get_netaddr(ifn):
    dic = {}
    dic['ip'] = get_ip_address(ifname=ifn)
    dic['mac'] = get_mac_addr(ifname=ifn)
    return dic


# 获取网卡名称和其ip地址，不包括回环
def get_netcard():
    netcard_info = []
    info = psutil.net_if_addrs()
    for k, v in info.items():
        for item in v:
            if item[0] == 2 and not item[1] == '127.0.0.1':
                netcard_info.append((k, item[1]))
    return netcard_info


print(get_netcard())
print(get_netaddr('eth1'))
print(get_netaddr('docker0'))
print(get_netaddr('lo'))
