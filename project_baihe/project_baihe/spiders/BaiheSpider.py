# coding:utf8
import scrapy
from ..items import ProjectBaiheItem
from .auto_mail import AutoMail
import os
import datetime

class BaiheSpider(scrapy.Spider):
    name = 'baihe'
    cookies = {'accessID':'20170531191244394021',
               'Hm_lvt_5497f3e5cf06014777f01fb0307e58f4':'1496229165',
               'tempID':'4940923599',
               'cookie_pcc':'1%7C%7Cbaidu-pp%7C%7C350002-001%7C%7Chttp%3A//bzclk.baidu.com/adrc.php%3Ft%3D06KL00c00fZaFKC00UNu0Q-HAsKJuAwu00000K_ndH300000L-W_JZ.THvsvUo51x60UWdBmy-bIy9EUyNxTAT0T1d-n1fknHcLnH0snj0vPWnd0ZRqnWTsfRwjnW9aPDFArDP7fHPjP1fdn19AP103nWfLPHm0mHdL5iuVmv-b5HnsnjR1n1n3rjfhTZFEuA-b5HDv0ARqpZwYTjCEQLILIz4Bmy-Cui4WUvYE5LKEUA-WXHYkFbPCmy48uysqmh7GuZRVTZ0hfvqbuHY1PH0snjcVnj0k0APzm1YYnW0vP6%26tpl%3Dtpl_10087_15653_1%26l%3D1054149659%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E7%252599%2525BE%2525E5%252590%252588%2525E7%2525BD%252591%28Baihe.com%29%25253A%252520%2525E5%2525AE%25259E%2525E5%252590%25258D%2525E8%2525AE%2525A4%2525E8%2525AF%252581%2525E4%2525BC%25259A%2525E5%252591%252598%252520%2526xp%253Did%28%252522m68b6bbea%252522%29%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D199%26wd%3D%25E7%2599%25BE%25E5%2590%2588%25E7%25BD%2591%26issp%3D1%26f%3D3%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26inputT%3D2758%26prefixsug%3D%2525E7%252599%2525BE%2525E5%252590%252588%26rsp%3D0',
               'channel':'baidu-pp',
               'code':'350002-001',
               'accessToken':'BH1501483428238119715',
               'lastLoginDate':'Mon%20Jul%2031%202017%2014%3A43%3A53%20GMT+0800%20%28%u4E2D%u56FD%u6807%u51C6%u65F6%u95F4%29',
               'orderSource':'10130301',
               'AuthCookie':'4BFFD62B611D896EFE3F42DDBE4FA60AD36B0CDB3346548EA61068A08F66F0DE9C2EF9ED4EE296CC904AF051C2A81FF4D7A6E2425F8EA85813DF4553FEF214B6066FB64698D168506BFB0F813A653583',
               'AuthMsgCookie':'315A61347AD71BC4E55ECB2A7E65E1F225204E6E3FF7375A401D6176CB5B36DE344C5868D33370A7450A04BF3A594E3E735C364DF685025CAE0B7CD1A11F4595F58D909F4960B7059EC7CF29BD1CB8BA',
               'GCUserID':'150896661',
               'OnceLoginWEB':'150896661',
               'LoginEmail':'15038703223%40mobile.baihe.com',
               'userID':'150896661',
               'spmUserID':'150896661',
               'AuthCheckStatusCookie':'10C7F889BAD64C4816F9F1F997D9E79514D1D3015978705726A127B203C4931405E9D878DCC812E7',
               'Hm_lvt_5caa30e0c191a1c525d4a6487bf45a9d':'1500294710,1500706398,1500712716,1501483428',
               'Hm_lpvt_5caa30e0c191a1c525d4a6487bf45a9d':'1501484235',
               '150896661_log':'1',
               '__asc':'eb10e2ad15d976f4898aa7a2c5c',
               '__auc':'1eae65e215c70c5d55de556aee4',
               'nTalk_CACHE_DATA':'{uid:kf_9847_ISME9754_150896661}',
               'NTKF_T2D_CLIENTID':'guestBC956C56-E011-A3AA-354A-5E3552570D91',
               'noticeEvent_150896661':'31',
               '_fmdata':'0DFB8355707802A947D56E1EC2081F43C054179C274A054947950A7CBC5F935E71711381ED1945DCDE2CD28023554A3ED98D8A78735BAD87'
               }
    # 错误页面
    url_error = ['http://profile1.baihe.com/static/html/account_close.html',
                 'http://profile1.baihe.com/static/html/account_busy.html']
    count = 0
    def start_requests(self):
        self.mail = AutoMail()
        urls = ['http://profile1.baihe.com/?oppId={}&showType=2012'.format(i) for i in range(80000000, 85000000)]
        for url in urls:
            yield scrapy.Request(url, cookies=self.cookies)

    def empty(self, tell):
        return True if tell else False

    def value(self, url):
        return url[0] if url else u''

    def parse(self, response):
        print("-- -- ", response.url)
        if response.url not in self.url_error:
            item = ProjectBaiheItem()
            item['ID'] = response.url.split('&')[0].split('=')[-1]
            man_woman = response.xpath("//div[@class='profileTopLeft']")
            # print item['ID']
            if self.empty(man_woman):
                vip = man_woman.xpath("//dl[@class='small_data']")
                if self.empty(vip):
                    item['vip'] = u'yes'
                    item['love_type'] = vip.xpath('dt[2]/text()').extract()[0]
                else:
                    item['vip'] = u'no'
                    item['love_type'] = man_woman.xpath("//div[@class='manPic']/dl/dt[2]/text()").extract()[0]
                item['url'] = man_woman.xpath("//div[@class='small_pic']/ul/li/img/@src").extract() if man_woman.xpath(
                    "//div[@class='small_pic']/ul/li/img/@src")else u''
                profile1 = response.xpath("//div[@class='profileTopRight']")
                item['nickname'] = profile1.xpath('div/span[2]/text()').extract()[0]
                item['name'] = u''
                item['label'] = ','.join(
                    profile1.xpath("//div[@class='inter label']/span/text()").extract()) if self.empty(
                    profile1.xpath("//div[@class='inter label']")) else u''
                # 年龄  身高  学历  城市
                infos = profile1.xpath("//div[@class='inter']/p/text()").extract()
                item['age'] = infos[0]
                item['height'] = infos[1]
                item['education'] = infos[2]
                item['city'] = infos[3]
                # 月薪  职业  星座  婚姻  住房  购车  属相  家乡
                infos1 = profile1.xpath("//div[@class='data']/dl[1]/dd/text()").extract()
                infos2 = profile1.xpath("//div[@class='data']/dl[2]/dd/text()").extract()
                item['marital_status'] = infos2[3]
                item['zodiac'] = infos1[2]
                item['hometown'] = infos1[3]
                item['constellation'] = infos2[2]
                item['occupation'] = infos2[1]
                item['monthly_salary'] = infos2[0]
                item['purchase'] = infos1[0]
                item['car_Buying'] = infos1[1]

                profile2 = response.xpath("//div[@class='profileLeft']")
                # 个人及工作状况
                infos1 = profile2.xpath("//div[@class='perData']/dl[1]/dd/text()").extract()
                infos2 = profile2.xpath("//div[@class='perData']/dl[2]/dd/text()").extract()
                item['registered_residence'] = infos1[0]
                item['blood_type'] = infos1[1]
                item['language'] = infos2[7]
                item['nation'] = infos1[4]
                item['graduation_school'] = infos2[2]
                item['major'] = infos2[3]
                item['religion'] = infos1[6]
                item['children'] = infos1[8]
                item['shape'] = infos1[3]
                item['self_assessment'] = infos1[5]
                item['weight'] = infos1[2]
                item['company'] = infos2[4]
                item['company_industry'] = infos2[5]
                item['working_condition'] = infos2[6]
                item['drink_status'] = infos2[1]
                item['smoke_status'] = infos2[0]
                item['life_style'] = infos1[7]
                # 自我介绍
                item['introduce_oneself'] = profile2.xpath("//div[@class='intr']/text()").extract()[0].strip()
                # 家庭状况&爱情规划
                item['about_family'] = ','.join(
                    profile2.xpath("//div[@class='perData']/dl[3]/dd/text()").extract()) + ','.join(
                    profile2.xpath("//div[@class='perData']/dl[4]/dd/text()").extract())
                # 择偶意向
                item['requirement'] = ','.join(
                    profile2.xpath("//div[@class='perData']/dl[5]/dd/text()").extract()) + ','.join(
                    profile2.xpath("//div[@class='perData']/dl[6]/dd/text()").extract())
                # item['requirement'] = ','.join(profile2.xpath("//div[@class='profileLeft']//div[@class='perData']/dl[5]/dd/text()").extract())
                # 经济实力
                item['economic_strength'] = u''
                # 爱好
                item['hobby'] = ','.join(profile2.xpath("//div[@class='cont']/em/text()").extract()) if self.empty(
                    profile2.xpath("//div[@class='profileLeft']//div[@class='cont']")) else u''
                # 百合
                item['resource'] = u'百合网'
                print('loading_' + item['ID'])
                # if (datetime.datetime.now().hour == 17 or datetime.datetime.now().hour == 42) and datetime.datetime.now().minute == 46 and datetime.datetime.now().second < 2:
                #     counts = str(datetime.datetime.now())+ "爬取数量：" + str(self.count)
                #     self.mail.send_mail("爬虫状态", counts)
                yield item
                # print item['ID'],item['nickname'],item['vip'],item['love_type'],item['label'],item['age'],item['height'],item['education'],item['city'],item['registered_residence'],item['language'],item['nation'],item['graduation_school'],item['weight'],item['occupation'],item['monthly_salary'],item['company'],item['purchase'],item['company_industry'],item['car_Buying'], item['working_condition'], item['drink_status'], item['smoke_status'], item['introduce_oneself'], item['about_family'],item['requirement'], item['life_style'], item['economic_strength'],item['hobby'], item['resource']
            else:
                # 图片
                item['url'] = u'' if response.xpath("//div[@class='noPic']") else response.xpath(
                    "//div[@class='womanPic']//img//@src").extract()
                # item['love_type'] = response.xpath("//div[@class='womanData']//dt[2]/text()").extract()[0]
                # 年龄  身高  学历  城市 婚姻
                profile1 = response.xpath("//div[@class='womanData']")
                # vip
                item['vip'] = u'yes' if profile1.xpath("//div[@class='data']//dt/img") else u'no'
                item['love_type'] = profile1.xpath("//dt[2]/text()").extract()[0]
                item['nickname'] = profile1.xpath("//div[@class='name']/span[2]/text()").extract()[0]
                item['name'] = u''
                infos = profile1.xpath("//div[@class='inter'][2]/p/text()").extract()
                item['age'] = infos[0]
                item['height'] = infos[1]
                item['education'] = infos[2]
                item['city'] = infos[3]
                item['marital_status'] = infos[4]
                item['label'] = ','.join(
                    profile1.xpath("//div[@class='inter label']/span/text()").extract()) if self.empty(
                    profile1.xpath("//div[@class='inter label']")) else u''

                profile2 = response.xpath("//div[@class='profileLeft']")
                # 自我介绍
                item['introduce_oneself'] = profile2.xpath("//div[@class='intr']/text()").extract()[0].strip()
                # 个人工作及状况
                infos1 = profile2.xpath("//div[@id='information']/dl[1]/dd/text()").extract()
                infos2 = profile2.xpath("//div[@id='information']/dl[2]/dd/text()").extract()
                item['registered_residence'] = infos1[0]
                item['language'] = infos2[0]
                item['nation'] = infos1[1]
                item['graduation_school'] = infos2[1]
                item['hometown'] = infos1[2]
                item['major'] = infos2[2]
                item['zodiac'] = infos1[3]
                item['religion'] = infos2[3]
                item['constellation'] = infos1[4]
                item['life_style'] = infos2[4]
                item['blood_type'] = infos1[5]
                item['children'] = infos2[5]
                item['shape'] = infos1[6]
                item['self_assessment'] = infos2[6]
                item['weight'] = infos1[7]
                item['smoke_status'] = infos2[7]
                item['occupation'] = infos1[8]
                item['drink_status'] = infos2[8]
                item['monthly_salary'] = infos1[9]
                item['company'] = infos2[9]
                item['purchase'] = infos1[10]
                item['company_industry'] = infos2[10]
                item['car_Buying'] = infos1[11]
                item['working_condition'] = infos2[11]
                item['economic_strength'] = u''
                # 家庭状况&爱情规划
                item['about_family'] = ','.join(profile2.xpath("//div[@id='information']/dl[3]/dd/text()").extract()) + ','.join(profile2.xpath("//div[@id='information']/dl[4]/dd/text()").extract())
                # 择偶意向
                item['requirement'] = ','.join(profile2.xpath("//div[@class='perData']/dl[1]/dd/text()").extract()) + ','.join( profile2.xpath("//div[@class='perData']/dl[2]/dd/text()").extract())
                item['hobby'] = ','.join(profile2.xpath("//div[@class='cont']/em/text()").extract()) if self.empty(profile2.xpath("//div[@class='profileLeft']//div[@class='cont']")) else u''
                # 百合
                item['resource'] = u'百合网'
                print('loading_' + item['ID'])
                # if (datetime.datetime.now().hour == 17 or datetime.datetime.now().hour == 42) and datetime.datetime.now().minute == 46 and datetime.datetime.now().second < 2:
                #     counts = str(datetime.datetime.now())+ "爬取数量：" + str(self.count)
                #     self.mail.send_mail("爬虫状态", counts)
                yield item
        else:
            print('account closed or busy')
