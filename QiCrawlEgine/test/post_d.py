
# coding:utf8
import requests
import json

'''
爬虫引擎测试
'''
data = {
    'id': '1',
    'Jobid': '25814',
    'Jobname': 'xiaozhu爬虫',
    'Username': '田康博',
    'Template': '小猪短租',
    'State': '1',
    'Keyword': '北京,2017-10-15,2017-10-19',
    'Searchdate': '0',
    'Starttime': '0',
    'Endtime': '0',
}

headers = {'Content-Type': 'application/json'}
r = requests.post(url='http://localhost:8000/request', headers=headers, data=json.dumps(data))
print(r.text)