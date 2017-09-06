# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import MySQLdb
from store_csv import CSV

class LagouzpPipeline(object):
    # #写文件
    def __init__(self):
        firstRow = ['职位名称', '公司名称', '城市', '公司规模', '公司类型', '月薪', '行业领域', 'firstType', 'senondType', '工作经历', '学历', '发布时间']
        self.write = CSV('lagou.csv', firstRow)

    def process_item(self, item, spider):
        row = [item['name'], item['city'], item['company_name'], item['size'], item['financeStage'],item['salary'], item['industryField'], item['firstType'],item['secondType'],item['workYear'],item['edu'],item['time']]
        self.write.writeRow(row)
        return item
    #数据库
    # def __init__(self):
    #     self.conn = MySQLdb.connect(user='root', passwd='pa$$w0rd', db='lagou', host='localhost', charset='utf8',
    #                                 use_unicode=True)
    #     self.cursor = self.conn.cursor()
    #
    # def process_item(self, item, spider):
    #     self.cursor.execute(
    #         "insert into jobinfo(name,city,company,size,type,salary,field,firsttype,secondtype,workyear,edu,time) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(item['name'], item['city'], item['company_name'], item['size'], item['financeStage'],item['salary'], item['industryField'], item['firstType'],item['secondType'],item['workYear'],item['edu'],item['time'],))
    #     self.conn.commit()
    #     return item

