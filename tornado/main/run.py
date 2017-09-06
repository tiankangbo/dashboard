# import sys
# import os.path
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.gen

from tornado.options import define, options


define("port", default=8000, help="run on the given port", type=int)

from pymongo import MongoClient

settings = {
    "ip":'127.0.0.1',
    "port":27017,
    "db_name" : "mydb",
    "set_name" : "test_set"
}

class MyMongoDB(object):
    def __init__(self, input):
        try:
            self.conn = MongoClient(settings["ip"], settings["port"])
            self.dic = input
        except Exception as e:
            print(e)
        self.db = self.conn[settings["db_name"]]
        self.my_set = self.db[settings["set_name"]]

    def insert(self):
        self.my_set.insert(self.dic)

    def delete(self):
        self.my_set.remove(self.dic)

    def dbfind(self):
        data = self.my_set.find(self.dic)
        for result in data:
            print(result["name"],result["age"])


class RequestHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def param_(self, data):
        try:
            msg = eval(data)
            print("msg", msg)
            # mongo = MyMongoDB(msg)
            # mongo.insert()

        except:
            print("error")

    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        try:
            '''from get get all args'''
            args = self.request.arguments
            self.write(args)
            # yield self.param_(data=args)
        except:
            with open('getException.txt', 'a') as f:
                f.write('get exception')
            f.close()

    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        try:
            '''from post get all args'''
            data = self.request.body
            # yield self.param_(data=data)
            msg = eval(data)
            print("msg", msg)
            # mongo = MyMongoDB(msg)
            # mongo.insert()
            # self.write(data)
        except:
            with open('postException.txt', 'a') as f:
                f.write('post exception')
            f.close()


app = tornado.web.Application(handlers=[
    (r"/request/", RequestHandler),
])

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()