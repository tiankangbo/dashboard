# coding:utf8
__author__ = 'tiankangbo'

import requests
from bs4 import BeautifulSoup

# 设置头请求
headers = {
        "User-Agent":'Mozilla/5/0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
        }

weather_code = {
        "北京":"101010100",
        "上海":"101020100",
        }
city = input("请输入一所城市(北京，上海)")

# 需要爬取的网址
#http://www.weather.com.cn/weather/101190101.shtml
url = "http://www.weather.com.cn/weather/{}.shtml".format(weather_code[city])
#url = "http://forecast.weather.com.cn/town/weather1dn/101181004012.shtml#input"
# 发送头请求，获取一个response对象

responsefile = requests.get(url, headers=headers)

# 设置responsefile.text编码
responsefile.encoding = 'utf-8'
# 得到网页源代码
content = responsefile.text
# 使用lxml解析器来创建Soup对象
soup = BeautifulSoup(content, 'lxml')

# 使用CSS select()语法获取天气温度，首先要分析网页
tag_list = soup.find_all("p", class_="tem")

for tag in tag_list:
    print(tag)
    responsefile = 0



