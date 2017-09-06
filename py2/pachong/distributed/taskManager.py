#!/usr/bin/env python
# encoding: utf-8

"""
author : tiankangbo
date : 2017-07-19
"""

import random, time, Queue
from multiprocessing.managers import BaseManager

# 第一步建立task_queue和result_queue, 用来存放任务和结果
task_queue = Queue.Queue()
result_queue = Queue.Queue()


class Queuemanager(BaseManager):
    pass
# 第二步把创建的两个队列注册到网络上，利用register方法，callable参数关联了Queue对象
# 将Queue对象在网络中暴露
Queuemanager.register('get_task_queue', callable=lambda:task_queue)
Queuemanager.register('get_result_queue', callable=lambda:result_queue)


# 第三步绑定端口8001, 设置验证口令‘qiye’，即对象的初始化
manager=Queuemanager(address=('', 8001), authkey='qiye')


# 第四步，启动管理监听信息通道
manager.start()

# 第五步通过管理实例的方法获得通过网络访问的Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()


# 第六步添加任务
for url in ["ImageUrl_"+bytes(i) for i in range(10)]:
    print 'put task %s ' % url
    task.put(url)

# 获取返回结果
print '-----try get result '
for i in range(10):
    print 'result is %s ' % result.get(timeout=10)


#关闭管理
manager.shutdown()




