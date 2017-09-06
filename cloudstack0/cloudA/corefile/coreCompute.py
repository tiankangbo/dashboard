#!/usr/bin/env python
# coding:utf8

import base64
import hashlib
import hmac
import urllib
import urllib2
import cloudA.corefile.readjson

base_url = cloudA.corefile.readjson.usage_command("baseurl")
api_key = cloudA.corefile.readjson.usage_command("apikey")
secret_key = cloudA.corefile.readjson.usage_command("secretkey")


def request_str(request1):
    '''获取未经过编码计算的完整的请求命令串'''
    return '&'.join(['='.join([k, urllib.quote_plus(request1[k])]) for k in request1.keys()])


def sig_str(request2, secret):
    '''获取经过urllib编码和base64和hmac加密计算签名值'''
    sig_s = '&'.join(['='.join([k.lower(), urllib.quote_plus(request2[k].lower().replace('+', '%20'))]) for k in sorted(request2.iterkeys())])
    return urllib.quote_plus(base64.encodestring(hmac.new(secret, sig_s, hashlib.sha1).digest()).strip())


def get_url(request):
    '''获取完整的请求URL串, 返回请求数据'''
    request_str_s = request_str(request)
    sig = sig_str(request, secret_key)
    req = base_url + request_str_s + '&signature=' + sig
    return req


def get_dict(dict1):
    '''合并两个字典, 一个本地的字典, 一个参数传递过来的字典'''
    dict2 = {'response': 'json', 'apikey': api_key}
    dict_all = dict(dict1, **dict2)
    return dict_all


def requests(dt):
    '''获得url的响应'''
    t = get_dict(dt)
    url1 = get_url(t)
    return urllib2.urlopen(url1).read()

if __name__ == '__main__':
    dict1 = {'command': 'listUsers'}
    print requests(dict1)
