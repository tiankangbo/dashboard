#!/usr/bin/env python
# encoding: utf-8

"""
author : tiankangbo
data : 2017-07-24
"""

import requests

r = requests.get('http://www.baidu.com')

print(r.content)
