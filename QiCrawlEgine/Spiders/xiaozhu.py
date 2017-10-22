import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'
}

# 城市映射  拼接URL
cities = {
    '北京': 'beijing',
    '上海': 'shanghai',
    '广州': 'guangzhou',
    '成都': 'chengdu',
    '三亚': 'sanya',
    '厦门': 'xiamen',
    '青岛': 'qingdao',
    '深圳': 'shenzhen',
    '重庆': 'chongqing',
    '杭州': 'hangzhou',
    '昆明': 'kunming',
    '大理': 'dali',
    '丽江': 'lijiang',
    '西安': 'xian',
    '天津': 'tianjin',
    '哈尔滨': 'haerbin',
    '珠海': 'zhuhai',
    '济南': 'jn',
    '南京': 'nanjing',
    '武汉': 'wuhan',
    '苏州': 'suzhou',
    '长沙': 'changsha'
}


class XiaoZhu(object):
    url = 'http://{}.xiaozhu.com/search-duanzufang-p{}-0/'

    # 参数
    params = {
        'startDate': '',
        'endDate': ''
    }

    # get请求  返回源码
    def get_g_request(self, url=''):
        if url == '':
            if self.params['startDate'] == '':
                html = requests.get(self.url, headers=headers)
            else:
                html = requests.get(self.url, params=self.params, headers=headers)
        else:
            html = requests.get(url, headers=headers)
        # print(html.url)
        return html.text

    # 获取页面房源连接
    def house_list(self):
        data = etree.HTML(self.get_g_request())
        links = data.xpath('//div[@id="page_list"]/ul/li/a/@href')
        for link in links:
            yield self.details(self.get_g_request(link))

    # 房源信息页面解读  参数：源码
    def details(self, html):
        detail = {}
        info = etree.HTML(html)
        #地点
        detail['house_address'] = info.xpath('//div[@class="pho_info"]/p/span/text()')[0].split('\n')[0]
        # 面积
        detail['house_area'] = info.xpath('//div[@id="introducePart"]/ul/li[1]/p/text()')[0].split('：')[-1]
        # 房屋类型
        detail['house_type'] = info.xpath('//div[@id="introducePart"]/ul/li[1]/p/text()')[1].split('：')[-1].strip()
        # 宜住
        detail['house_suit'] = info.xpath('//div[@id="introducePart"]/ul/li[2]/h6/text()')[0]
        # 床位数
        detail['bed_count'] = info.xpath('//div[@id="introducePart"]/ul/li[3]/h6/text()')[0]
        # 床位细节描述  存的是列表
        detail['bed_detail'] = [bed.strip() for bed in info.xpath('//div[@id="introducePart"]/ul/li[3]/p/text()')]
        # 个性描述
        detail['diy_describe'] = ('').join(
            [a.strip() for a in info.xpath('//div[@id="introducePart"]/div[1]/div[2]/div/p/text()')])
        # 内部情况
        detail['situation_in'] = ('').join(
            [a.strip() for a in info.xpath('//div[@id="introducePart"]/div[2]/div[2]/div/p/text()')])
        # 交通情况
        detail['traffic_situation'] = ('').join(
            [a.strip() for a in info.xpath('//div[@id="introducePart"]/div[3]/div[2]/div/p/text()')])
        # 周边情况
        detail['around_situation'] = ('').join(
            [a.strip() for a in info.xpath('//div[@id="introducePart"]/div[4]/div[2]/div/p/text()')])
        # 配套设施
        detail['house_device'] = [device.strip() for device in
                                  info.xpath('//div[@id="introducePart"]/div[5]/div[2]/div/ul/li/text()')]
        # 入住须知
        detail['lived_know'] = [thing for thing in
                                info.xpath('//div[@id="introducePart"]/div[6]/div[2]/div/ul/li/text()')]
        # 押金及其他费用
        detail['pay_other'] = [thing.strip() for thing in info.xpath('//div[@id="rulesPart"]/div/p/text()')]
        detail['pay_other'].append(info.xpath('//div[@id="rulesPart"]/div/div/text()')[0].strip())
        # 每天的价格（单价）
        detail['house_pay'] = info.xpath('//div[@id="pricePart"]/div/span/text()')[0]
        # 评分
        try:
            detail['comment'] = info.xpath('//div[@id="comment_box"]/div/div/span/text()')[0]
        except:
            detail['comment'] = '本房源暂无评分'
        yield detail

    # 分页
    def div_page(self, city):
        for page in range(1, 4):
            self.url = self.url.format(cities[city], str(page))
            # print(self.url)
            yield self.house_list()

    # 程序入口
    def run(self, lt):
        city = lt.split(',')[0]
        startDate = lt.split(',')[1]
        endDate = lt.split(',')[2]

        self.params['startDate'] = startDate
        self.params['endDate'] = endDate
        test = self.div_page(city)
        for one in test:
            for on in one:
                for o in on:
                    yield o
                    # print(o)

if __name__ == "__main__":
    xiaozhu = XiaoZhu()
    xiaozhu.run('北京,2017-10-20,2017-10-25')
