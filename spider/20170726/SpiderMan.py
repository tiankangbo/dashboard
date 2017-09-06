# coding:utf8

from DataOutput import DataOutput
from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser
from URLManager import UrlManager


class SpiderMan(object):
    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    def crawl(self, root_url):
        # 添加入口url
        self.manager.add_new_url(root_url)
        # 判断url管理器中是否有新的url，同时判断抓取了多少个url
        while(self.manager.has_new_url() and self.manager.old_url_size()<200):
            try:
                #从url管理器中获取url
                new_url = self.manager.get_new_url()
                # html下载器下载网页
                html = self.downloader.download(new_url)
                #html解析器抽取网页数据
                new_urls, data = self.parser.parser(new_url, html)
                # 将抽取的url放到url管理器中
                self.manager.add_new_urls(new_urls)
                # 将抽取的数据存储起来
                self.output.store_data(data)
                print " 已经抽取了 %s 个链接" % self.manager.old_url_size()
            except Exception, e:
                print "crawl failed", e

        self.output.output_html()

if __name__ == '__main__':
    spider_man = SpiderMan()
    #spider_man.crawl("http://baike.baidu.com/view/284853.htm")
    spider_man.crawl("http://baike.baidu.com/view/284853.htm")
