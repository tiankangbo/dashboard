#!/usr/bin/env python
# encoding: utf-8

"""
author: tiankangbo
data: 2017-07-19
email: tiankangbo@gmail.com
"""

import random
import threading
import time

class myThread(threading.Thread):
    def __init__(self, name, urls):
        threading.Thread.__init__(self, name=name)
        self.urls = urls

    def run(self):
        print 'current %s is running ' % threading.current_thread().name
        for url in self.urls:
            print '%s------->>>%s' % (threading.current_thread().name, url)
            time.sleep(random.random())
        print '%s end ' % threading.current_thread().name

print '%s is running ' % threading.current_thread().name

t1 = myThread(name='thread_1', urls=['url1', 'url2', 'url3',])
t2 = myThread(name='thread_2', urls=['url4', 'url5', 'url6',])

t1.start()
t2.start()

t1.join()
t2.join()

print '%s is end ' % threading.current_thread().name



