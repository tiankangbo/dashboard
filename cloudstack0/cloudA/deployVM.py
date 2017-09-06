#!/usr/bin/env python
# coding:utf8

from cloudA.corefile import coreCompute, readjson
from cloudA.dataview import writejson

command_cloud1 = readjson.usage_command("command_deployVM")
command_cloud2 = readjson.usage_command("templateId")
command_cloud3 = readjson.usage_command("serviceOfferingId")
command_cloud4 = readjson.usage_command("zoneId")


if __name__ == '__main__':
    request_1 = {'command': command_cloud1, 'templateId': command_cloud2, 'serviceOfferingId': command_cloud3, 'zoneId': command_cloud4}
    lt = coreCompute.requests(request_1)
    writejson.store(lt)