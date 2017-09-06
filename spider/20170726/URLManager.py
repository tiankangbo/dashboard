# coding:utf8
"""
URL管理器
"""
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()  # 未爬取的URL集合
        self.old_urls = set()  # 已经爬取的url集合

    def has_new_url(self):
        """
        判断是否有未爬取的URL
        :return:
        """
        return self.new_url_size() != 0

    def get_new_url(self):
        """
        获取一个新未爬取的URL
        :return:
        """
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def add_new_url(self, url):
        """
        将新的url添加到未爬取的url集合中
        :param url: 单个url
        :return:
        """
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        """
        将新的url添加到未爬取的url集合中
        :param urls: url集合
        :return:
        """
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def new_url_size(self):
        """
        获取未爬取的URL集合大小
        :return:
        """
        return len(self.new_urls)

    def old_url_size(self):
        """
        获取已经爬取的URL集合大小
        :return:
        """
        return len(self.old_urls)