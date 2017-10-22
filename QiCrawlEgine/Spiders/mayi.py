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
    '秦皇岛': 'qinhuangdao',
    '三亚': 'sanya',
    '厦门': 'xiamen',
    '青岛': 'qingdao',
    '大连': 'dalian',
    '威海': 'weihai',
    '深圳': 'shenzhen',
    '重庆': 'chongqing',
    '杭州': 'hangzhou',
    '葫芦岛': 'huludao',
    '昆明': 'kunming',
    '大理': 'dali',
    '丽江': 'lijiang',
    '西安': 'xian',
    '天津': 'tianjin',
    '哈尔滨': 'haerbin',
    '珠海': 'zhuhai',
    '南京': 'nanjing',
    '武汉': 'wuhan',
    '苏州': 'suzhou',
    '长沙': 'changsha',
    '日照': 'rizhao',
    '烟台': 'yantai',
    '营口': 'yingkou',
    '北海': 'beihai',
    '乌鲁木齐': 'wulumuqi',
    '沈阳': 'shenyang',
    '丹东': 'dandong',
    '济南': 'jinan',
    '承德': 'chengde',
    '大阪': 'daban',
    '京都': 'jingdu',
    '洛阳': 'luoyang',
    '开封': 'kaifeng',
    '新乡': 'xinxiang',
    '郑州': 'zhengzhou',
    '香港': 'xianggang',
}


class MaYi(object):
    old = 'http://www.mayi.com'
    url = 'http://www.mayi.com/{}/{}/'  # 网站url

    # 日期参数
    params = {
        'd1': '',
        'd2': '',
    }

    # get请求  返回源码

    def get_g_request(self, url=''):

        if url == '':
            if self.params['d1'] == '':
                html = requests.get(self.url, headers=headers)
            else:
                html = requests.get(self.url, params=self.params, headers=headers)
        else:
            html = requests.get(url, headers=headers)

        return html.text

    # 获取页面房源连接

    def house_list(self):
        data = etree.HTML(self.get_g_request())
        links = data.xpath('//*[@id="searchRoom"]/dd/a/@href')

        for link in links:
            yield self.details(self.get_g_request(self.old + link))

    # 获取详情信息

    def details(self, html):
        detail = {}
        info = etree.HTML(html)

        # 房源介绍
        house_m = info.xpath('//*[@class="zhan_off"]/div/h4/text()')
        house_tl = info.xpath('//*[@class="zhan_off"]/div/p/text()')

        detail['房源介绍'] = dict(zip([i for i in house_m], [''.join(str.split()) for str in house_tl if ''.join(str.split()) not in ['', None]]))

        # 房源名字
        detail['房源名字'] = info.xpath('//*[@id="photo"]/div[1]/h2/a[1]/text()')[0]

        # 房源地址
        detail['房源地址'] = info.xpath('//*[@id="photo"]/div[1]/p/text()')[0]

        # 房源状况
        detail['房源状况'] = [''.join(info.xpath('//*[@id="photo"]/div[2]/div[2]/ul/li[1]/p/text()')[0].split()),
                          ''.join(info.xpath('//*[@class="w258"]/p/text()')[0].split()),
                          ''.join(info.xpath('//*[@class="w258"]/p/span/text()')[0].split()),
                          ]
        # 基本信息
        data_f = info.xpath('//*[@class="table fl fl_p"]/li/text()')
        data_g = info.xpath('//*[@class="table fl fl_p"]/li/span/text()')

        detail['基本信息'] = dict(zip(
            [''.join(str.split()) for str in data_f if ''.join(str.split()) not in ['', None]],
            [''.join(str.split()) for str in data_g if ''.join(str.split()) not in ['', None]]
        ))

        # 配套设施
        detail['配套设施'] = [''.join(i.split()) for i in info.xpath('//*[@class="intro sup_fac padding_t clearfloat"]/ul/li/text()') if ''.join(i.split()) not in ['', None]]

        # 租价
        detail['租价/晚'] = info.xpath('//*[@class="priceL"]/span/text()')[0]

        # 好评率
        detail['好评率'] = info.xpath('//*[@class="C_00897b font24"]/text()')

        yield detail

    # 分页

    def get_page(self, city):
        for page in range(1, 6):
            self.url = self.url.format(cities[city], str(page))
            yield self.house_list()

    # 程序入口
    def run(self, lt):
        address = lt.split(',')[0]
        start = lt.split(',')[1]
        end = lt.split(',')[2]

        self.params['d1'] = start
        self.params['d2'] = end

        test = self.get_page(address)

        for one in test:
            for a in one:
                for b in a:
                    yield b
                    # print(b)

if __name__ == '__main__':
    a = MaYi()
    dic = a.run('北京,2017-10-25,2017-10-29')

    num = 1
    while dic.__next__:
        data = next(dic)
        num = num + 1
        print("num -- == ", num, data)