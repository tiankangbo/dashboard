# coding:utf8
import queue

lt = queue.Queue()
lt.put_nowait('1')
lt.get_nowait()