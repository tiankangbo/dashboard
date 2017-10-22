# coding:utf8
import requests
import json

'''
爬虫引擎测试
'''
data = {
    'id': '247',
    'Jobid': '25814',
    'Jobname': 'mayi爬虫',
    'Username': '田康博',
    'Template': '蚂蚁短租',
    'State': '1',
    'Keyword': '北京,2017-10-25,2017-10-29',
    'Searchdate': '0',
    'Starttime': '0',
    'Endtime': '0',
}

headers = {'Content-Type': 'application/json'}
r = requests.post(url='http://localhost:8000/request', headers=headers, data=json.dumps(data))
print(r.text)