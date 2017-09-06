#!/usr/bin/env python
# encoding: utf-8

import requests

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent':user_agent}

r = requests.get('http://www.baidu.com', headers=headers)

#遍历出所有cookie字段的值

for cookie in r.cookies.keys():
    print(cookie + ":" + r.cookies.get(cookie))
