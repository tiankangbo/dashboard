# coding:utf8
import requests
import json

'''
爬虫引擎测试
'''
data = {
    'id': '249',
    'Jobid': '0',
    'Jobname': '51Job爬虫',
    'Username': '田康博',
    'Template': '前程无忧',
    'State': '1',
    'Keyword': 'java开发工程师,上海',
    'Searchdate': '0',
    'Starttime': '0',
    'Endtime': '0',
}

headers = {'Content-Type': 'application/json'}
r = requests.post(url='http://localhost:8000/request', headers=headers, data=json.dumps(data))
print(r.text)