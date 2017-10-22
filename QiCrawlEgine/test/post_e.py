
# coding:utf8
import requests
import json

'''
爬虫引擎测试
'''
data = {
    'id': '248',
    'Jobid': '25814',
    'Jobname': 'aibizhi爬虫123',
    'Username': '田康博',
    'Template': '爱壁纸',
    'State': '1',
    'Keyword': '动物宠物',
    'Searchdate': '0',
    'Starttime': '0',
    'Endtime': '0',
}

headers = {'Content-Type': 'application/json'}
r = requests.post(url='http://localhost:8000/request', headers=headers, data=json.dumps(data))
print(r.text)