# coding:utf-8
import json


def store(data):
    with open('/home/tiankango/PycharmProjects/cloudstack0/cloudA/dataview/request_data.json', 'w') as json_fp:
        json_fp.write(json.dumps(data))
    json_fp.close()