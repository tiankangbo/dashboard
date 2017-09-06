from scrapy import log, signals
from scrapy.crawler import Crawler
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor

from testspiders.spiders.followall import FollowAllSpider

spider = FollowAllSpider(domain='scrapinghub.com')
settings = get_project_settings()
crawler = Crawler(settings)
crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
crawler.configure()
crawler.crawl(spider)
crawler.start()
log.start()
reactor.run()

# from twisted.internet import reactor
# from scrapy.crawler import CrawlerRunner
# from scrapy.utils.project import get_project_settings
#
# runner = CrawlerRunner(get_project_settings())
# print "running ***", runner
# # 'followall' is the name of one of the spiders of the project.
# d = runner.crawl('followall', domain='scrapinghub.com')
# d.addBoth(lambda _: reactor.stop())
# reactor.run() # the script will block here until the crawling is finished
#
# print "test"