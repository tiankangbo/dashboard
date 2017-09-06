# coding:utf8
from __future__ import print_function

__author__ = 'tiankangbo'

"""
该Spider是为了取爬取虎嗅网上的一些标题、资料简述、发布时间、以及网页链接
"""

from SCspiders.items import HuxiuItem
import scrapy
import time

class Huxiu(scrapy.Spider):

    name = "huxiu"
    allowd_domains = ["huxiu.com"]
    start_urls = {
        "http://www.huxiu.com/index.php"
    }


    def parse(self, response):
        for sel in response.xpath('//div[@class="mod-info-flow"]/div/div[@class="mob-ctt"]'):
            url = response.urljoin(sel.xpath('h2/a/@href')[0].extract())
            print("-- -- ", url)

            yield scrapy.Request(url=url, callback=self.parse_article)


    def parse_article(self, response):
        # '//div[@class="article-wrap"]/div/p/span[@class="text-remarks"]/text()'
        item = HuxiuItem()

        detail = response.xpath('//div[@class="container"]/div[@class="wrap-left pull-left"]/div[@class="article-wrap"]')
        detail_1 = response.xpath('//div[@class="container"]/div[@class="wrap-right pull-right"]')
        item['title'] = detail.xpath('h1/text()')[0].extract()
        item['posttime'] = detail.xpath('div/div/span[@class="article-time pull-left"]/text()')[0].extract()
        item['author'] = detail.xpath('div/span/a/text()')[0].extract()
        item['nexttitle'] = detail_1.xpath('div/div[@class="author-next-article"]/a/text()')[0].extract()
        item['link'] = response.url
        item['instime'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

        yield item