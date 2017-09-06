# coding:utf8
__author__ = 'tiankangbo'
'''
THIS IS A Crawler
'''

from urllib.request import urlopen
import json

html = urlopen("http://pythonscraping.com/pages/page1.html")


print(html.read())
