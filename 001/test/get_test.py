# coding:utf8
import requests

url = "http://localhost:8002/sleep"

r = requests.get(url=url)

print(r.text)