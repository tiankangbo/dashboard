from lxml import etree
import requests
import os

cities = {
    '武汉': '180200',
    '宁波': '080300',
    '昆明': '250200',
    '苏州': '070300',
    '成都': '090200',
    '福州': '110200',
    '东莞': '030800',
    '西安': '200200',
    '长沙': '190200',
    '深圳': '040000',
    '郑州': '170200',
    '重庆': '060000',
    '大连': '230300',
    '上海': '020000',
    '天津': '050000',
    '青岛': '120300',
    '哈尔滨': '220200',
    '杭州': '080200',
    '广州': '030200',
    '南京': '070200',
    '沈阳': '230200',
    '北京': '010000',
    '济南': '120200',
    '合肥': '150200',
    '长春': '240200'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'
}


class QianCheng(object):
    # URL
    url = 'http://search.51job.com/list/{},000000,0000,00,9,99,{},2,{}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='


    def get_g_req(self, url=''):
        if url == '':
            html = requests.get(self.url, headers=headers).text
        else:
            html = requests.get(url, headers=headers).content
        return html

    # 获取所有职位URL
    def all_link(self, html):
        data = etree.HTML(html)
        links = data.xpath('//div[@id="resultList"]/div[@class="el"]/p/span/a/@href')
        for link in links[1:]:
            yield self.detail_page(self.get_g_req(link))

        # 详情页信息

    def detail_page(self, html):
        detail = {}
        data = etree.HTML(html)
        info1 = data.xpath('//div[@class="tHeader tHjob"]/div/div[@class="cn"]')[0]
        # 职位名
        detail['work_name'] = info1.xpath('h1/text()')[0]
        # 公司名
        detail['company_name'] = info1.xpath('p/a/text()')[0]
        # 地点
        detail['work_site'] = info1.xpath('span/text()')[0]
        # 月薪
        try:
            detail['month_salary'] = info1.xpath('strong/text()')[0]
        except:
            detail['month_salary'] = '未知'
        # 职位要求  列表
        detail['people_need'] = data.xpath('//div[@class="tCompany_main"]/div/div/div/span/text()')
        # detail['work_experience'] = data.xpath('//div[@class="tCompany_main"]/div/div/div/span[1]/text()')[0]
        # detail['degree'] = data.xpath('//div[@class="tCompany_main"]/div/div/div/span[2]/text()')[0]
        # detail['people_count'] = data.xpath('//div[@class="tCompany_main"]/div/div/div/span[3]/text()')[0]
        # detail['publish_time'] = data.xpath('//div[@class="tCompany_main"]/div/div/div/span[4]/text()')[0]

        # 福利
        try:
            detail['fuli'] = data.xpath('//div[@class="tCompany_main"]/div/div/p[@class="t2"]/span/text()')
        except:
            detail['fuli'] = ['无福利']
        # 上班地点
        detail['work_addr'] = data.xpath('//div[@class="tCompany_main"]//div[@class="tBorderTop_box"]/div/p/text()')[
            1].strip() if len(
            data.xpath('//div[@class="tCompany_main"]//div[@class="tBorderTop_box"]/div/p/text()')) > 1 else '未提供地址'
        yield detail

    # 分页
    def div_page(self, city, kw):
        for page in range(1, 6):
            self.url = self.url.format(cities[city], kw, str(page))
            yield self.all_link(self.get_g_req())

        # 入口  城市 关键字

    def run(self, lt):
        city = lt.split(',')[1]
        kw = lt.split(',')[0]
        jobs = self.div_page(city, kw)
        for job in jobs:
            for one in job:
                for work in one:
                    # print(work)
                    yield work


if __name__ == "__main__":
    test = QianCheng()
    dic = test.run('python,上海')
    num = 1
    while dic.__next__:
        data = next(dic)
        num = num + 1
        print("num -- == ", num, data)
