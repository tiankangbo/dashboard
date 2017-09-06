# coding:utf8
__author__ = 'tiankangbo'

# import time
# import threading
#
#
# def func():
#     print "sleep 10"
#
#     time.sleep(5)
#
#
# if __name__ == '__main__':
#
#     for i in xrange(500):
#         t = threading.Thread(target=func, )
#         t.start()
import threading


def do(event):
    print "start"
    event.wait()
    print "execute"


event_obj = threading.Event()

for i in range(10):
    t = threading.Thread(target=do, args=(event_obj,))
    t.start()

event_obj.clear()


inp = raw_input("input: ")
if inp == 'true':
    event_obj.set()
