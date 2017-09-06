# coding:utf8
__author__ = 'Tiankangbo'


# class tianKangbo(Exception):
#     def __init__(self, msg):
#         self.message = msg
#
#     def __str__(self):
#         return self.message
#
# try:
#     raise tianKangbo('my exception')
#
# except tianKangbo, e:
#     print e

# from multiprocessing import Process, Array
#
# temp = Array('i', [11, 22, 33, 44])
#
#
# def Foo(i):
#     temp[i] = 100 + i
#     for item in temp:
#         print i, '----->', item
#
#
# for i in range(2):
#     p = Process(target=Foo, args=(i,))
#     p.start()

# from multiprocessing import Process, Manager
#
# manage = Manager()
# dic = manage.dict()
#
#
# def Foo(i):
#     dic[i] = 100 + i
#     print dic.values()
#
#
# for i in range(2):
#     p = Process(target=Foo, args=(i,))
#     p.start()
#     p.join()


from multiprocessing import Process, Queue


def f(i,q):
    print(i, q.get())

if __name__ == '__main__':
    q = Queue()

    q.put("h1")
    q.put("h2")
    q.put("h3")

    for i in range(10):
        p = Process(target=f, args=(i,q,))
        p.start()
        p.join()
