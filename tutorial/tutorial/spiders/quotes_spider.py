# coding:utf8
__author__ = 'tiankangbo'

import scrapy
from tutorial.items import TutorialItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]

    start_urls = {
         "http://quotes.toscrape.com/page/1",
    }

    def parse(self, response):

        item = TutorialItem()

        # page = response.url.split("/")[-2]
        # 解析谚语
        # list = response.xpath(".//div/span[@class='text']/text()").extract()
        detail = response.xpath(".//div[@class='quote']")

        item['text'] = detail.xpath("span[@class='text']/text()").extract()
        item['author'] = detail.xpath("span/small/text()").extract()

        next_page = response.xpath('.//nav/ul/li[@class="next"]/a/@href').extract()[0]
        # print(item['text'], item['author'])
        yield item
        # 自动翻页
        if next_page:
            print('http://quotes.toscrape.com'+next_page)
            page_after = 'http://quotes.toscrape.com'+next_page
            yield scrapy.Request(url=page_after, callback=self.parse)

        # self.log('save file %s' % filename)
