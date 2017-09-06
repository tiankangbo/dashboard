# -*- coding:utf-8 -*-
from __future__ import print_function
from __future__ import print_function
import scrapy
from ..items import LagouzpItem
import requests
from bs4 import BeautifulSoup
import json

class Spider(scrapy.Spider):
    name = 'lagou'
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
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"}
    def start_requests(self):
        kd = ['python工程师', 'python数据分析']
        city = ['北京', '上海', '深圳', '广州', '杭州', '成都', '南京', '武汉', '西安', '厦门', '长沙', '苏州', '天津']
        urls_kd = ['https://www.lagou.com/jobs/list_{}?px=default&city='.format(one) for one in kd]
        for urls in urls_kd:
            urls_city = [urls + one for one in city]
            for url in urls_city:
                response = requests.get(url, headers=self.headers, cookies=self.cookies)
                location = url.split('&')[-1].split('=')[1]
                key = url.split('/')[-1].split('?')[0].split('_')[1]
                soup = BeautifulSoup(response.text, 'lxml')
                pages = soup.find('span', {'class': 'span totalNum'}).get_text()
                for i in range(1, int(pages) + 1):
                    url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city={}&needAddtionalResult=false'.format(location)
                    formdata = {
                        'first': 'true',
                        'pn': str(i),
                        'kd': key
                    }
                    print(u'正在获取职位——{}，城市{},第{}页数据'.format(key, location, i))
                    yield scrapy.FormRequest(url,formdata=formdata,cookies=self.cookies,callback=self.parse)
    def parse(self, response):
        data = json.loads(response.text)
        print("data -- -- -- ", data)


        # content = data['content']
        # positionResult = content['positionResult']
        # item = LagouzpItem()
        # for one in positionResult['result']:
        #     try:
        #         item['city'] = one['city']
        #     except:
        #         item['city'] = u''
        #     try:
        #         item['company_name'] = one['companyFullName']
        #     except:
        #         item['company_name'] = u''
        #     try:
        #         item['size'] = one['companySize']
        #     except:
        #         item['size'] = u''
        #     try:
        #         item['edu'] = one['education']
        #     except:
        #         item['edu'] = u''
        #     try:
        #         item['financeStage'] = one['financeStage']
        #     except:
        #         item['financeStage'] = u''
        #     try:
        #         item['firstType'] = one['firstType']
        #     except:
        #         item['firstType'] = u''
        #     try:
        #         item['industryField'] = one['industryField']
        #     except:
        #         item['industryField'] = u''
        #     try:
        #         item['name']= one['positionName']
        #     except:
        #         item['name'] = u''
        #     try:
        #         item['salary'] = one['salary']
        #     except:
        #         item['salary'] = u''
        #     try:
        #         item['secondType'] = one['secondType']
        #     except:
        #         item['secondType'] = u''
        #     try:
        #         item['workYear'] = one['workYear']
        #     except:
        #         item['workYear'] = u''
        #     try:
        #         item['time'] = one['createTime'].split(' ')[0]
        #     except:
        #         item['time'] = u''
        #     yield item