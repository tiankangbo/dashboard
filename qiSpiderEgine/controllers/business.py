# coding:utf8

import web

render = web.template.render('static/html/')

from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor, defer
import scrapy
from scrapy.crawler import CrawlerProcess


class Index:
    def GET(self):
        # return open(r'static/index.html').read()
        # 跳转欢迎页面
        return render.index()

    def POST(self):
        pass


def start():
    runner = CrawlerRunner(get_project_settings())
    print("running ***", runner)
    d = runner.crawl('huxiu')

    d.addBoth(lambda _: reactor.stop())
    reactor.run()

    print("test")


class start:
    def GET(self):
        # i = web.input()
        # do = i.name
        # print "so -- >", do
        # if do == 'start':
        runner = CrawlerRunner(get_project_settings())
        print("running ***", runner)

        d = runner.crawl('huxiu')

        d.addBoth(lambda _: reactor.stop())
        reactor.run()
        # process = CrawlerProcess(get_project_settings())
        # process.crawl(input)
        # process.start()
        # print("test")

        import multiprocessing

        qc = multiprocessing.Process(target=start, args=())
        qc.start()
        qc.join()


class stop:
    pass


class getMessage:
    pass

    # a = start()
    # a.GET()
