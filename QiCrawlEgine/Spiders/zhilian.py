import requests
from lxml import etree
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'
}


class ZhiLian(object):
    # 搜索URL
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx'

    # get请求参数
    params = {
        # 'pd':1, #发布日期
        'jl': '北京',  # 地点
        'kw': 'java工程师',  # 关键字
        'p': 1,  # 分页
        'st': 99999,
        'sm': 0,  # 显示方式
        'sf': 0,
        'isadv': 1  # 高级检索
    }

    # 请求返回页面源码
    def get_r_rq(self):
        data = requests.get(self.url, params=self.params, headers=headers)
        return data.text

    # 详情页信息
    def work_detail(self, url):
        details = {}
        datas = etree.HTML(requests.get(url, headers=headers).text)
        # 工作名称
        details['work_name'] = datas.xpath('//div[@class="inner-left fl"]/h1/text()')[0]
        # 公司名称
        details['company_name'] = datas.xpath('//div[@class="inner-left fl"]/h2//a/text()')[0]
        infos = datas.xpath('//div[@class="terminalpage-left"]/ul/li/strong')
        # 月薪
        details['month_salary'] = infos[0].xpath('text()')[0].strip()
        # 工作地点
        details['company_location'] = infos[1].xpath('a/text()')[0]
        # 发布日期
        details['publish_time'] = infos[2].xpath('span/text()')[0]
        # 工作性质
        details['work_nature'] = infos[3].xpath('text()')[0]
        # 工作经验
        details['work_experience'] = infos[4].xpath('text()')[0]
        # 学历
        details['work_level'] = infos[5].xpath('text()')[0]
        # 招聘人数
        details['people_needs'] = infos[6].xpath('text()')[0]
        # 工作类别
        details['work_type'] = infos[7].xpath('a/text()')[0]
        # 工作地址
        try:
            details['work_address'] = datas.xpath('//div[@class="tab-inner-cont"]/h2/text()')[0].strip()
        except:
            details['work_address'] = '未知'
        yield details

    # 招聘职位列表   URL
    def work_url_list(self, data):
        # detail = {}
        datas = etree.HTML(data)
        infos = datas.xpath('//*[@id="newlist_list_div"]/div[1]/table')
        for info in infos[1:]:
            url = info.xpath('tr/td[1]/div/a/@href')[0]
            yield self.work_detail(url)

    # 分页
    def del_page(self):
        for i in range(1, self.page + 1):
            self.params['p'] = i
            try:
                yield self.work_url_list(self.get_r_rq())
            except:
                print('......error')

    # 运行（传入 关键字  地点）
    def run(self, lt):
        kw = lt.split(',')[0]
        addr = lt.split(',')[1]

        self.page = 10
        self.params['kw'] = kw
        self.params['jl'] = addr

        test = self.del_page()
        for one in test:
            for o in one:
                for i in o:
                    # print(i)

                    yield i


if __name__ == "__main__":
    test = ZhiLian()
    dic = test.run('java,北京')
    num = 1
    while dic.__next__:
        data = next(dic)
        num = num + 1
        print("num -- == ", num, data)
