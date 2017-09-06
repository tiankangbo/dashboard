# coding:utf8
__author__ = 'tiankangbo'

import cPickle
import hashlib


class UrlManager(object):
    def __init__(self):
        self.new_urls = self.load_progress('new_urls.txt')
        self.old_urls = self.load_progress('old_urls.txt')

    def has_new_url(self):
        """
        判断是否有未爬取的url集合
        :return:
        """
        return self.new_url_size() != 0

    def get_new_url(self):
        """
        获取一个未爬取的url
        :return:
        """
        new_url = self.new_urls.pop()
        m = hashlib.md5()
        m.update(new_url)
        self.old_urls.add(m.hexdigest()[8:-8])
        return new_url

    def add_new_url(self, url):
        """
        将新的url添加到未爬取的url集合中
        :param url: 单个的url
        :return:
        """
        if url is None:
            return
        m = hashlib.md5()
        m.update(url)
        url_md5 = m.hexdigest()[8:-8]
        if url not in self.new_urls and url_md5 not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        """
        将新的url放到未爬取的url集合中
        :param urls: urls集合
        :return:
        """
        if urls is None or len(urls) == 0:
            return

        for url in urls:
            self.add_new_url(url)

    def new_url_size(self):
        """
        获取未爬取URL集合大小
        :return:
        """
        return len(self.new_urls)

    def old_url_size(self):
        """
        获取已经爬取的URL集合大小
        :return:
        """
        return len(self.old_urls)

    def save_process(self, path, data):
        """
        保存进度
        :param path:文件路径
        :param data: 数据
        :return:
        """
        with open(path, 'wb') as f:
            cPickle.dump(data, f)

    def load_process(self, path):
        """
        本地文件加载进度
        :param path:文件路径
        :return: 返回set集合
        """
        print "[+] 从文件加载进度 %s" % path
        try:
            with open(path, 'rb') as f:
                tmp = cPickle.load(f)
                return tmp
        except Exception, e:
            print "[!] 无进度文件， 创建：%s" % path

        return set()
