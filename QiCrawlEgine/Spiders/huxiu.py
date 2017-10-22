import requests
import time
import random
from lxml import etree

headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'

}

cates = {
    '电商消费': '103.html',
    '娱乐淘金': '22.html',
    '雪花一代': '106.html',
    '人工智能': '104.html',
    '车与出行': '21.html',
    '智能终端': '105.html',
    '金融地产': '102.html',
    '医疗健康': '111.html',
    '企业服务': '110.html',
    '创业维艰': '2.html',
    '社交通讯': '112.html',
    '全球热点': '107.html',
    '生活腔调': '4.html'
}


class HuXiu(object):
    def __init__(self):
        pass

    def get_p_data(self, page=2):
        '''
        :param page: 按照页码获取下一页的数据, 初始化页码为2
        :return:
        '''
        data = {
            'huxiu_hash_code': '8108c2df22264a5769c3a50798622c16',
            'page': page,
            'catId': self.catId
        }
        html = requests.post('https://www.huxiu.com/channel/ajaxGetMore', headers=headers, data=data)
        time.sleep(1)
        data = html.json()
        data = data['data']['data']
        return data

    def get_detail(self, html):
        '''
        :param html: 直接获取详情数据, html->页面数据
        :return: 抓取定制的数据, 并将数据存放至字典,返回给上级程序.
        '''
        data = etree.HTML(html)
        container = data.xpath('//div[@class="article-wrap"]')[0]
        title = container.xpath('h1/text()')[0].strip()
        author = container.xpath('div/span/a/text()')[0]
        pub_time = container.xpath('div[1]/div[1]/span[1]/text()')[0] if container.xpath(
            'div[1]/div[1]/span[1]/text()') else '未知'
        content = ('').join(data.xpath('//div[@class="article-content-wrap"]/p/text()'))

        return {
            'title': title,
            'author': author,
            'pubtime': pub_time,
            'content': content
        }

    def get_g_request(self, url):
        '''
        :param url:
        :return: 根据url, 获取文章text
        '''
        self.catId = url.split('/')[-1].split('.')[0]
        time.sleep(1)
        html = requests.get(url, headers=headers)
        return html.text

    def get_url(self, data):
        '''
        :param data: 页面数据
        :return: 数据存放到生成器
        '''
        data = etree.HTML(data)
        href = data.xpath('//div[@class="mob-ctt"]/h2/a/@href')
        for url in href:
            link = 'https://www.huxiu.com' + url
            time.sleep(1)
            yield self.get_detail(requests.get(link, headers=headers).text)

    def get_more_ajax(self, page=5):

        data = {
            'huxiu_hash_code': '8108c2df22264a5769c3a50798622c16',
            'page': 2,
            'catId': self.catId
        }
        html = requests.post('https://www.huxiu.com/channel/ajaxGetMore', headers=headers, data=data)
        data = html.json()
        time.sleep(random.randint(1, 5))
        '''获取总页码'''
        total_page = int(data['data']['total_page'])
        if total_page < page:
            for page_per in range(2, total_page + 1):
                yield self.get_url(self.get_p_data(page_per))
        else:
            for page_per in range(2, page + 1):
                yield self.get_url(self.get_p_data(page_per))

    def get_search_result(self, data):
        '''
        :param data:
        :return:
        '''
        result = etree.HTML(data)
        urls = ['https://www.huxiu.com' + url for url in
                result.xpath('//ul[@class="search-wrap-list-ul"]/li/h2/a/@href')]
        return urls

    def get_search_url(self, keyword):
        '''
        :param keyword: 自定义的关键字
        :return: 数据存储到生成器,并返回
        '''
        url = 'https://www.huxiu.com/search.html?s=' + keyword + '&per_page={}'
        urls = [url.format(i) for i in range(1, 6)]
        for url in urls:
            for link in self.get_search_result(self.get_g_request(url)):
                yield self.get_detail(self.get_g_request(link))

    def run(self, keyword):
        '''
        :param keyword:  关键字的传入
        :return: 接受Api的调度
        '''
        if keyword in cates.keys():
            url = 'https://www.huxiu.com/channel/' + cates[keyword]
            self.catId = url.split('/')[-1].split('.')[0]
            # self.get_url(self.get_g_request(url))
            tests2 = self.get_more_ajax()

            for ones in tests2:
                for one in ones:
                    yield one
        else:
            result = self.get_search_url(keyword)
            for ones in result:
                yield ones


if __name__ == "__main__":
    huxiu = HuXiu()

    # huxiu.get_url(huxiu.get_g_request(url))
    # huxiu.get_more_ajax()

    huxiu.run('电商消费')
