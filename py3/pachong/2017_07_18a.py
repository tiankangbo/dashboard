# coding:utf8
__author__ = 'tiankangbo'

from multiprocessing import Pipe, Process
import random
import time, os


def proc_send(pipe, urls):
    """
    pipe的发送端
    :param pipe:
    :param urls:
    :return:
    """
    for url in urls:
        print("process %s --send %s " %(os.getpid(), url) )
        pipe.send(url)
        time.sleep(random.random())


def proc_recv(pipe):
    """
    数据接收端
    :param pipe:
    :return:
    """
    while True:
        print('process %s >>>rev%s ' % (os.getpid(), pipe.recv()))
        time.sleep(random.random())


if __name__ == '__main__':
    pipe = Pipe()

    p1 = Process(target=proc_send, args=(pipe[0], ['url_'+str(i) for i in range(10)],))
    p2 = Process(target=proc_recv, args=(pipe[1],))

    #启动进程
    p1.start()
    p2.start()

    p1.join()
    p2.terminate()