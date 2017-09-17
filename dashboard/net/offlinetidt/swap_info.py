# coding:utf8
"""
-------------------------------------------------
   File Name：     swap_info.py
   Description :  功能：统计swap的总空间，使用空间，剩余空间，统计单位MB
   Author :       tiankangbo
   date：         2017/3/13
-------------------------------------------------
   Change Activity:
-------------------------------------------------
"""
import psutil

def fun_swap():

    list_swap = []

    swap_message = psutil.swap_memory()
    swap_total = swap_message.total
    swap_used = swap_message.used
    swap_free = swap_message.free
    #swap_percent = swap_message.percent

    list_swap.append(str(swap_total/1024/1024))
    list_swap.append(str(swap_used/1024/1024))
    list_swap.append(str(swap_free/1024/1024))
    #list_swap.append(str(swap_percent)+'%')

    return list_swap

if __name__ == '__main__':
    print "总大小---使用量---空余量------>使用百分比"
    print fun_swap()
