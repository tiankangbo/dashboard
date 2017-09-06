# coding:utf8
import requests
import json

data = {
    'jobid': 1234567832,
    'jobname': 'huxiuSpider',
    'username':'tiankangbo',
    'template':'huxiu',
    'state':'1',
    'keyword':'huawei',
    'starttime':'20170829',
    'endtime':'20170830',
}

headers = {'Content-Type': 'application/json'}
r = requests.post(url='http://localhost:8002/sleep', headers=headers, data=json.dumps(data))
print(r)
print(r.text)