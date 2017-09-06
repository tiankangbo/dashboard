from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings

runner = CrawlerRunner(get_project_settings())
print "running ***", runner
# 'followall' is the name of one of the spiders of the project.
d = runner.crawl('huxiu')

d.addBoth(lambda _: reactor.stop())
reactor.run() # the script will block here until the crawling is finished

print "test"