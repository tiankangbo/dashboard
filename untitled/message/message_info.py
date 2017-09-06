from datetime import datetime, timedelta
import time

def compute(day=0, hour=0, min=0, second=0):

    print "hello"
    n = 1
    now = datetime.now()
    period = timedelta(days=day, hours=hour, minutes=min, seconds=second)
    next_time = now + period

    while True:

        time.sleep(second)
        iter_now = datetime.now()

        if (next_time-iter_now <= period):
            n = n + 1
            print "number ", n
            #print "yes"

            #yield fun_sub(list1_1, list1), fun_sub(list2_2, list2)

            next_time = iter_now + period
            continue


compute(day=0, hour=0, min=0, second=5)