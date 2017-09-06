#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "tiankangbo"


from wsgiref.simple_server import make_server


def index():
    f = open('index.html')
    data = f.read()
    return data


def login():
    fp = open('login.html')
    data = fp.read()
    return data


def routers():
    urlpatterns = (
        ('/index/', index),
        ('/login/', login),
    )
    return urlpatterns


def run_server(environ, start_response):
    start_response('400 OK', [('Content-Type', 'text/html')])
    url = environ['PATH_INFO']
    print "url ->", url

    urlpatterns = routers()
    print "urlpatterns ->", urlpatterns

    func = None

    for item in urlpatterns:
        if item[0] == url:
            func = item[1]
            break
    if func:
        return func()
    else:
        return '404 not Found'


if __name__ == '__main__':
    httpd = make_server('', 8000, run_server)
    print "Serving HTTP on port 8000 ---"
    httpd.serve_forever()


