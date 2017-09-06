#!/usr/bin/env python
# encoding: utf-8

"""
author : tiankangbo
date : 2017-07-19
"""

import time
from multiprocessing.managers import BaseManager

# 创建类似的QueueManager
class QueueManager(BaseManager):
    pass

# 第一步使用QueueManager注册用于获取Queue的方法名称
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 第二步连接到服务器
server_addr = '127.0.0.1'
print 'connect to server %s ' % server_addr

# 端口和验证口令，注意保持一致
m = QueueManager(address=(server_addr, 8001), authkey='qiye')

#从网络连接
m.connect()

#第三步获取queue的对象
task = m.get_task_queue()
result = m.get_result_queue()

#第四步，从task队列中获取任务，并把结果写入到result队列
while(not task.empty()):
    image_url = task.get(True, timeout=5)
    print 'run task download %s ' % image_url
    time.sleep(1)
    result.put('%s --- success ' % image_url)

print 'work exit'

