# coding:utf8

import urllib2
import cookielib

url = 'http://mail.163.com/'
cookie = cookielib.CookieJar()

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

response = opener.open(url)

for item in cookie:
    print item.name + ': ' + item.value