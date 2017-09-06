#!/usr/bin/env python
# encoding: utf-8

"""
author : tiankangbo
data : 2017-07-19
"""

from gevent import monkey; monkey.patch_all()
import gevent
import urllib2


def run_task(url):
    print 'visit -->%s ' % url
    try:
        response = urllib2.urlopen(url)
        data = response.read()
        print '%d bytes received from %s ' %(len(data), url)
    except Exception, e:
        print e

if __name__ == '__main__':
    urls = ['https://github.com', 'https://www.python.org', 'http://www.cnblogs.com/']
    greenlets = [gevent.spawn(run_task, url) for url in urls ]
    gevent.joinall(greenlets)
