# coding:utf8
__author__ = 'tiankangbo'

from multiprocessing import Process, Queue
import os, time, random


def proc_write(q, urls):
    """
    向queue中写入数据
    :param q:
    :param urls:
    :return:
    """
    print('process %s is writing....' % os.getpid())
    for url in urls:
        q.put(url)
        print('put %s to queue' % url)
        time.sleep(random.random())


def proc_read(q):
    """
    从队列里面读取数据
    :param q:
    :return:
    """
    print('process %s is reading...' % os.getpid())
    while True:
        url = q.get(True)
        print('get %s from queue' % url)


if __name__ == '__main__':

    q = Queue()
    write1 = Process(target=proc_write, args=(q, ['url1', 'url2', 'url3',],))
    write2 = Process(target=proc_write, args=(q, ['url4', 'url5', 'url6',],))

    read1 = Process(target=proc_read, args=(q,))

    # 启动进程
    write1.start()
    write2.start()
    read1.start()

    # 等待进程结束
    write1.join()
    write2.join()

    # read1进程是死循环，不能等待结束，只能强制结束
    read1.terminate()