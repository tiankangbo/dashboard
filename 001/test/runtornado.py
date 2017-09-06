# coding:utf8
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from multiprocessing import Process
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import tornado.gen
from tornado.concurrent import run_on_executor
# 这个并发库在python3自带;在python2需要安装sudo pip install futures
from concurrent.futures import ThreadPoolExecutor
from scrapy.utils.project import get_project_settings
import scrapy
from scrapy.crawler import CrawlerProcess, CrawlerRunner
from tornado.concurrent import run_on_executor
from twisted.internet import reactor, defer
from scrapy.utils.log import configure_logging


from tornado.options import define, options

define("port", default=8002, help="run on the given port", type=int)


class MyProcess(Process):
    def __init__(self, input):
        Process.__init__(self)
        # self.jobname = input['jobname']
        self.username = input['username']
        self.template = input['template']
        # self.state = input['state']
        # self.keyword = input['keyword']

    @tornado.gen.coroutine
    def run(self):
        # print('pid --- -- > ' + str(self.pid))
        @defer.inlineCallbacks
        def crawl():
            configure_logging()
            runner = CrawlerRunner(get_project_settings())
            yield  runner.crawl(self.template)
            reactor.stop()

        crawl()
        reactor.run()



class SleepHandler(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(max_workers=128)

    def post(self, *args, **kwargs):
        data = self.request.body
        self.write(data)
        self.dic = eval(data)
        self.db = self.dic['username']
        self.my_set = self.dic['template']
        print("dic -- ", self.dic)
        tornado.ioloop.IOLoop.instance().add_callback(self.doJob)

    @run_on_executor
    def doJob(self):
        from mongo.mongocli import MyMongoDB
        mongo = MyMongoDB(self.db, self.my_set)
        mongo.insert(self.dic)

        jobname = MyProcess(self.dic)
        jobname.daemon = True
        jobname.start()
        jobname.join()


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/sleep", SleepHandler),])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()