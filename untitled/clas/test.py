# coding:utf8

import threading

# class Person(object):
#
#     def __init__(self):
#         print "init persion"
#
#     def speak(self):
#         print "speak"


def speak():
    print "$$$$$$"

def time_clock():
    while True:
        timer = threading.Timer(1, speak,)
        print "start"

        timer.start()
        timer.join()

        print "end"

if __name__ == '__main__':

#    p = Person()
    time_clock()

