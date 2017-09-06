#!/usr/bin/env python
# encoding: utf-8
"""
author : tiankangbo
data : 2017-07-24
"""

import urllib2

request = urllib2.Request("http://www.baidu.com")
#print request

response = urllib2.urlopen(request)
html = response.read()
print html
