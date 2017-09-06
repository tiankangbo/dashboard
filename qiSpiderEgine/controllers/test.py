import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
import scrapy
from scrapy.crawler import CrawlerProcess, CrawlerRunner
from twisted.internet import reactor, defer
from scrapy.utils.log import configure_logging

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):

    def start(self, input):
        runner = CrawlerRunner(get_project_settings())
        print("running ***", runner)
        d = runner.crawl(input)

        d.addBoth(lambda _: reactor.stop())
        reactor.run()

        print("test")

    def get(self, input):
        # greeting = self.get_argument('greeting', 'hello')
        # self.write(greeting + ', friendly user!')
        # print("--->", input)
        # process = CrawlerProcess(get_project_settings())
        # process.crawl('huxiu')
        # process.start()

            # configure_logging()
            # runner = CrawlerRunner()
            #
            # @defer.inlineCallbacks
            # def crawl(input):
            #     yield runner.crawl(input)
            #     reactor.stop()
            #
            # crawl(input=input)
            # reactor.run()
        # yield self.start()
        # self.write(input)
        # import os
        import multiprocessing

        qc = multiprocessing.Process(target=self.start, args=(input,))
        qc.start()
        qc.join()


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/reverse/(\w+)", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()