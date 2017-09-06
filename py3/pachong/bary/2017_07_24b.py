#!/usr/bin/env python
# encoding: utf-8

"""
生成二维码
"""

import qrcode
img = qrcode.make("www.baidu.com")




img.save("./baidu.png")

