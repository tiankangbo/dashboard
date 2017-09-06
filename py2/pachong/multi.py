#!/usr/bin/env python
# encoding: utf-8

"""
author : tiankangbo
e-mail : tiankangbo@gmail.com
data : 2017-07-18
"""

from multiprocessing import Pool
import os, time, random

def run_task(name):
    print "task %s (pid=%s) is running ..." % (name, os.getpid())
    time.sleep(random.random()*3)
    print "task %s is end" % name

if __name__ == '__main__':
    print 'current process %s ' % os.getpid()
    p = Pool(3)
    for i in range(5):
        p.apply_async(run_task, args=(i,))
    print "wait all process done"
    p.close()
    p.join()
    print "all subprocesses done"

