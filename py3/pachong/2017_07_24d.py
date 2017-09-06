#!/usr/bin/env python
# encoding: utf-8

"""
author:tianakngbo
date : 2017-07-24
"""
import requests

payload = {'Keywords' : 'blog:qiyeboy', 'pageindex':1}

r = requests.get('http://zzk.cnblogs.com/s/blogpost', params=payload)
print(r.url)
