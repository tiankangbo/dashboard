# -*- coding: utf-8 -*-

from twisted.internet import defer, reactor
from twisted.internet.threads import deferToThread

import functools
import time

# 耗时操作 这是一个同步阻塞函数
def mySleep(timeout):
    time.sleep(timeout)

    # 返回值相当于加进了callback里
    return 3

def say(result):
    print("耗时操作结束了, 并把它返回的结果给我了", result)
    reactor.stop()


# 用functools.partial包装一下, 传递参数进去
cb = functools.partial(mySleep, 3)
d = deferToThread(cb)
d.addCallback(say)

print("你还没有结束我就执行了, 哈哈")

reactor.run()