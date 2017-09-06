# coding:utf8
# from __future__ import print_function

__author__= 'tiankangbo'

import scrapy
import time
from lagouZhaopin.items import LagouzhaopinItem

class LagoupositionSpider(scrapy.Spider):
    name = "lagou"
    start_urls = ['https://www.lagou.com/zhaopin/']

    cookies = {
            'showExpriedCompanyHome': '1',
            'PRE_SITE': 'https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DXJN0fEdNCLllXATbXNsDCr8NGIq-sPvwFxzGYyCYJR3%26wd%3D%26eqid%3De67dd7390000d31e00000004599411c8',
            'unick': '%E7%94%B0%E5%BA%B7%E5%8D%9A',
            'ab_test_random_num': '0',
            'PRE_UTM': '',
            '_putrc': 'B61B305B1714B19E',
            'index_location_city': '%E5%85%A8%E5%9B%BD',
            'LGRID': '20170816173545-4732b5e6-8266-11e7-bb48-525400f775ce',
            'JSESSIONID': 'ABAAABAAAGFABEF6960D69A8FE82FC7BC7993462192CEC7',
            'LGUID': '20170801091558-f95c7c3a-7656-11e7-8640-525400f775ce',
            'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1502876145',
            '_gid': 'GA1.2.1710908453.1502876042',
            'PRE_LAND': 'https%3A%2F%2Fwww.lagou.com%2F',
            'showExpriedIndex': '1',
            '_ga': 'GA1.2.830453536.1502876042',
            'showExpriedMyPublish': '1',
            'hasDeliver': '0',
            'PRE_HOST': 'www.baidu.com',
            '_gat': '1',
            'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1502876042,1502876109',
            'LGSID': '20170816173508-318116e9-8266-11e7-bb48-525400f775ce',
            'X_HTTP_TOKEN': '555e875413c9371c96bc542ffea7211b',
            'user_trace_token': '20170801091556-1bf1c45f-7f9f-4c28-9269-ff94665bbd8d',
            'login': 'true',
            'SEARCH_ID': '1b9d0144ea424844b30b16468708182f'
    }


    def start_requests(self):
        urls = ['https://www.lagou.com/zhaopin/{}/?filterOption=3'.format(
            i) if i > 1 else 'https://www.lagou.com/zhaopin/?filterOption=3' for i in range(1, 31)]

        for url in urls:
            print("url -> ", url)
            time.sleep(3)
            yield scrapy.Request(url=url, cookies=self.cookies)


    def parse(self, response):
        print("respon.url -- -- -- ", response)
        # jobList = response.xpath("//*[@id="s_position_list"]/ul")
        # urlList = jobList.xpath("li[1]/div[1]/div[1]/div[1]/a/@href")
        #
        # for job in jobList:
        #     pass
        #
        # for url in urlList:
        #     print("-- ",url)
            # yield scrapy.Request(url=url, cookies=self.cookies, callback=self.parse_data)


    # def parse_data(self, response):
    #
    #     item = LagouzhaopinItem()
    #     detail1 = response.xpath('//html/body/div[2]/div/div[1]')
    #     detail2 = response.xpath('//*[@id="job_detail"]')
    #     detail3 = response.xpath('//*[@id="job_company"]')
    #
    #     item['company'] = detail1.xpath('div/div[1]/text()').extract()
    #     item['jobname'] = detail1.xpath('div/span/text()').extract()
    #
    #     list_salary1 = detail1.xpath('dd/p[1]/span[1]/text()').extract()
    #     list_salary2 = detail1.xpath('dd/p[1]/span[2]/text()').extract()
    #     item['salary'] = list_salary1 + list_salary2    #'/html/body/div[2]/div/div[1]/dd/p[1]/span[1]'
    #
    #     list_person1 = detail1.xpath('dd/p[1]/span[3]/text()').extract()
    #     list_person2 = detail1.xpath('dd/p[1]/span[4]/text()').extract()
    #     list_person3 = detail1.xpath('dd/p[1]/span[5]/text()').extract()
    #     item['aboutperson'] = list_person1 + list_person2 + list_person3
    #
    #     item['jobdesc'] = detail2.xpath('dd[2]/div').extract()
    #
    #     list_addr1 =  detail2.xpath('dd[3]/div[1]/a[2]').extract()
    #     list_addr2 = detail2.xpath('dd[3]/div[1]/a[3]').extract()
    #     list_addr3 = detail2.xpath('dd[3]/div[1]/text()').extract()
    #     item['address'] = list_addr1 + list_addr2 + list_addr3
    #
    #     list_company1 = detail3.xpath('dt/a/img/@alt').extract()
    #     list_company2 = detail3.xpath('dd/ul/li/text()').extract()
    #     item['aboutcompany'] = list_company1 + list_company2
    #
    #     item['posttime'] = detail1.xpath('dd/p[2]/text()').extract()
    #     item['instime'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    #
    #     yield item
