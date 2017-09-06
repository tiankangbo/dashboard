from multiprocessing import Process
import time
from twisted.internet import reactor, defer
from scrapy.utils.log import configure_logging

from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from tornado.options import define, options

class MyProcess(Process):
    def __init__(self, input):
        Process.__init__(self)
        self.input = input

    def run(self):
        # for count in range(self.loop):
        #     time.sleep(1)
        #     print('Pid: ' + str(self.pid) + ' LoopCount: ' + str(count))
        print('pid --- -- > ' + str(self.pid))
        configure_logging()
        runner = CrawlerRunner(get_project_settings())

        @defer.inlineCallbacks
        def crawl():
            yield runner.crawl(self.input)

            reactor.stop()

        crawl()
        reactor.run()

lt = []

if __name__ == '__main__':
    for i in range(3):
        print(i)
        p = MyProcess('huxiu')
        p.start()
        lt.append(p)

    for p in lt:p.join()
