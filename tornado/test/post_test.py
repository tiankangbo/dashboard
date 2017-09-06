import requests
import json

postdata = {
            'jobid': 1234567832,
            'jobname': 'huxiuSpider',
            'username':'tiankangbo',
            'template':'huxiu123',
            'state':'1',
            'keyword':'huawei',
            'starttime':'20170829',
            'endtime':'20170830',
            }

headers = {"Content-type": "application/json"}

r = requests.post(url="http://localhost:8000/request/", headers=headers, data=json.dumps(postdata))

print(r.text)