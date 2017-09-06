#!/usr/bin/env python
# encoding: utf-8

import random
import threading
import time

class myThread(threading.Thread):

    def __init__(self, name, urls):
        threading.Thread.__init__(self, name=name)
        self.urls = urls

    def run(self):
        print "%s is running " % threading.current_thread().name
        for url in self.urls:
            print "%s    --  %s" %(threading.current_thread().name, url)
            time.sleep(random.random())

t1 = myThread(name='Thread--1', urls=['url_1', 'url_2', 'url_3'])
t2 = myThread(name='Thread--2', urls=['url_3', 'url_4', 'url_5'])

t1.start()
t2.start()

t1.join()
t2.join()

print "end %s " % threading.current_thread().name


