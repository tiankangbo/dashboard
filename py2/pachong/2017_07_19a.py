#!/usr/bin/env python
# encoding: utf-8
"""
author:tiankangbo
data:2017-07-18a
email:tiankangbo@outlook.com
"""

import random
import time, threading

def thread_run(urls):
    """
    新线程执行代码块
    """
    print 'current %s is running ...' % threading.current_thread().name
    for url in urls:
        print '%s-------------->>%s' % (threading.current_thread().name, url)
        time.sleep(random.random())
    print '%s ..........end' % threading.current_thread().name

print '%s is running ' % threading.current_thread().name


t1 = threading.Thread(target=thread_run, name='Thread1', args=(['url1', 'url2', 'url3',],))
t2 = threading.Thread(target=thread_run, name='Thread2', args=(['url4', 'url5', 'url6',],))

t1.start()
t2.start()

t1.join()
t2.join()

print "%s is end " % threading.current_thread().name

