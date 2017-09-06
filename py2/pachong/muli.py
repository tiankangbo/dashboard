# coding:utf8
import urllib2
import json

data = {
    'jobid': 1234567832,
    'jobname': '虎嗅网爬虫',
    'username':'张三',
    'template':'虎嗅网',
    'state':'1',
    'keyword':'华为手机',
    'starttime':'20170829',
    'endtime':'20170830',
}

headers = {'Content-Type': 'application/json'}
request = urllib2.Request(url='http://localhost:8000/request/', headers=headers, data=json.dumps(data))
response = urllib2.urlopen(request)
print response.text
