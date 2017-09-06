# coding:utf8
__author__ ='tiankangbo'

from urllib.request import urlopen

from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page1.html")

bsObj = BeautifulSoup(html.read(), "lxml")

print(bsObj.html.h1)
