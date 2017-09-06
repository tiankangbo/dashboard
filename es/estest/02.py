# coding:utf-8

import pyes
import time
# from multiprocessing import Process

def create_conn():
    # 创建链接
    return pyes.ES(['192.168.10.52:9200'])


def new_index(i_conn, i_name):
    return i_conn.indices.create_index(i_name)


def get_now_time():
    # 获取现在的时间
    ttime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    return ttime


def data_structs():
    # 定义索引存储结构
    mapping = {
        u'property': {'boost': 1.0,
                      'index': 'analyzed',
                      'store': 'yes',
                      'type': u'string',
                      "term_vector": "with_positions_offsets"},
        u'name': {'boost': 1.0,
                  'index': 'analyzed',
                  'store': 'yes',
                  'type': u'string',
                  "term_vector": "with_positions_offsets"},
        u'time': {'boost': 1.0,
                  'index': 'analyzed',
                  'store': 'yes',
                  'type': u'string',
                  "term_vector": "with_positions_offsets"},
        u'size': {'store': 'yes',
                  'type': u'float'},
        u'path': {'boost': 1.0,
                  'index': 'not_analyzed',
                  'store': 'yes',
                  'type': u'string'}
    }
    return mapping


if __name__ == '__main__':

    try:

        conn = create_conn()#链接句柄
    except Exception, e:
        print e

    #新建一个索引
    #conn.indices.create_index('test-index')
    new_index(conn, "tiankangbo11")


    # 定义
    conn.indices.put_mapping("file", {'properties':data_structs()}, ["tiankangbo11"])#定义test-type
    #conn.indices.put_mapping("test-type2", {"_parent" : {"type" : "test-type"}}, ["test-index"])#从test-type继承

    #插入索引数据
    #{"name":"Python", "property":".doc", "path":"/var/lib", "size":1, "time":"2017-07-13"}: 文档数据
    #test-index：索引名称
    #test-type: 类型
    conn.index({"name":u"JAVA", "property":".doc", "path":"/var/lib", "size":5, "time":get_now_time()}, "tiankangbo11", "file")

    #conn.index({"name":"wanli15-year", "property":".mp4", "path":"/root", "size":2.1, "time":"2010-07-13"}, "tiankangbo11", "file")
    #conn.index({"name":"C++", "property":".pdf", "path":"/mnt", "size":11, "time":get_now_time()}, "tiankangtbo11", "file")

    conn.default_indices=[u"tiankangbo11"]#设置默认的索引
    conn.default_types=[u"file"]
    conn.indices.refresh()#刷新以获得最新插入的文档


    # q = pyes.TermQuery("name", u"Python")#查询name中包含bill的记录
    # results = conn.search(q)
    # for r in results:
    #     print "名字中包含Python的记录", r

    #查询name中包含C的数据
    q = pyes.QueryStringQuery(u".doc",'property')
    results = conn.search(q)
    for r in results:
        print "名字中包含C的数据", r

    q = pyes.QueryStringQuery(u"JAVA OR Python",'name')
    results = conn.search(q)
    for r in results:
        print "名字中包含JAVA or Python的数据", r