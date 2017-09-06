#!/usr/bin/env python
# encoding: utf-8

"""
author : tiankangbo
date : 2017-07-21
"""

import socket
import threading
import time


def delclient(sock, addr):
    """处理客户端链接"""
    print("new connect from %s : %s" % addr)
    sock.send(b"hello , i am server")
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        print("--->%s " % data.decode('utf-8'))
        sock.send(b'Loop from server')

    sock.close()
    print("connect  %s : %sis closed " % addr)


if __name__ == '__main__':

    """创建一个基于IPv4和TCP协议的socket
    并绑定本机的IP以及端口"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 9999))

    """建立监听"""
    s.listen(10)

    print(b"waiting for connect  " )

    while True:
        """接受一个新的链接"""
        sock, addr = s.accept()
        """创建新线程来处理TCP连接"""
        t = threading.Thread(target=delclient, args=(sock, addr, ))
        t.start()

