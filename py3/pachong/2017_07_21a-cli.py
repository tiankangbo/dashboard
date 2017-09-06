#!/usr/bin/env python
# encoding: utf-8

"""
author : tiankangbo
date : 2017-07-21
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


"""链接目标IP:port"""

s. connect(("127.0.0.1", 9999))

print("-->>>" + s.recv(1024).decode('utf-8'))

s.send(b"hello i am client")

s.send(b'exit')

s.close()


