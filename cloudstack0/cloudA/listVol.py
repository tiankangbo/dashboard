#!/usr/bin/env python
# coding:utf8

from cloudA.corefile import coreCompute, readjson
from cloudA.dataview import writejson

command_cloud = readjson.usage_command("command_listVol")


if __name__ == '__main__':
    request_1 = {'command': command_cloud}
    lt = coreCompute.requests(request_1)
    writejson.store(lt)