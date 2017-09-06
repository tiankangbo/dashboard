# coding:utf8
__author__ = 'tiankangbo'

import time
import threading

lock = threading.RLock()

class mythread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):

        lock.acquire()
        print "hello"
        time.sleep(3)
        lock.release()


if __name__ == '__main__':

    for i in xrange(100):

        t = mythread()
        t.start()