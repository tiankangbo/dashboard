import time
from elasticsearch import Elasticsearch


def get_now_time():
    ttime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    return ttime

def data_structs():
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
        es = Elasticsearch("192.168.10.51:9200")

        print es
    except Exception, e:
        print e

    #es.create("test-tiankangbo")


    #es.create("test-tiankangbo")
    #es.create(index="test-index", doc_type="test-type", id=1, body={"any": "data", "timestamp": get_now_time()})

    #es.indices.put_mapping("file", {'properties':data_structs()}, ["test-tiankangbo"])

    #es.index({"name":u"JAVA", "property":".doc", "path":"/var/lib", "size":5, "time":get_now_time()}, "test-tiankangbo", "file")
    print es.search("testdata", "hang", body={})
