# coding:utf8
from datetime import datetime, timedelta
import multiprocessing

def insert_fun2():

    print "c++"
    print "python"


def compute(fun, day=0, hour=0, min=0, second=0):

    fun()

    now = datetime.now()
    period = timedelta(days=day, hours=hour, minutes=min, seconds=second)
    next_time = now + period
    strnext_time = next_time.strftime('%Y-%m-%d %H:%M:%S')

    while True:
        # Get system current time
        iter_now = datetime.now()
        iter_now_time = iter_now.strftime('%Y-%m-%d %H:%M:%S')
        if str(iter_now_time) == str(strnext_time):

            fun()

            iter_time = iter_now + period
            strnext_time = iter_time.strftime('%Y-%m-%d %H:%M:%S')
            continue

if __name__ == '__main__':

    qq = multiprocessing.Process(target=compute, args=(insert_fun2, 0, 0, 0, 1,))
    qq.start()

