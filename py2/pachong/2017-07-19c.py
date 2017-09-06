#!/usr/bin/env python
# encoding: utf-8

"""
author : tiankangbo
date : 2017-07-19
email : tiankangbo@gmail.com
"""

import threading

mylock = threading.RLock()
num = 0

class myThread(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def run(self):
        global num
        while True:
            mylock.acquire()
            print '%s locked, number %d' % (threading.current_thread().name, num)

            if num >= 4:
                mylock.release()
                print '%s released , number %d' % (threading.current_thread().name, num)
                break

            num = num + 1
            print '%s released, number %d ' % (threading.current_thread().name, num)
            mylock.release()

if __name__ == '__main__':
    thread1 = myThread('thread--1')
    thread2 = myThread('thread-----2')

    thread1.start()
    thread2.start()
