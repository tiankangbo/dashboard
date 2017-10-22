# coding:utf8
import requests
import json

'''
爬虫引擎测试
'''
data = {
    'id': '3',
    'Jobid': '25814',
    'Jobname': 'huxiuSpider',
    'Username': '田康博',
    'Template': '虎嗅网',
    'State': '0',
    'Keyword': '全球热点',
    'Searchdate': '0',
    'Starttime': '0',
    'Endtime': '0',
}

headers = {'Content-Type': 'application/json'}
r = requests.post(url='http://localhost:8000/request', headers=headers, data=json.dumps(data))
print(r.text)