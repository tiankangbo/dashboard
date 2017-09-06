# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import uuid
import pymysql

class ProjectBaihePipeline(object):
    def __init__(self):
        #self.conn = pymysql.connect(user='admin', passwd='czhd_db', db='czhd', host='101.201.103.144', charset='utf8')
        self.conn = pymysql.connect(user='root', passwd='pa$$w0rd', db='spider', host='localhost', charset='utf8')
        self.cursor = self.conn.cursor()


    def process_item(self, item, spider):
        timeUUID = 'liang1' + str(uuid.uuid1())
        self.cursor.execute("insert into tbl_person2(UUID,ID,nickname,vip,love_type,label,age,height,education,city,marital_status,registered_residence,language,nation,graduation_school,hometown,major,zodiac,religion,constellation,blood_type,children,shape,self_assessment,weight,occupation,monthly_salary,company,purchase,company_industry,car_Buying,\
                              working_condition,drink_status,smoke_status,introduce_oneself,about_family,requirement,life_style,economic_strength,hobby,resource)\
                               values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                              (timeUUID,item['ID'],item['nickname'],item['vip'],item['love_type'],item['label'],item['age'].encode('utf-8'),item['height'],item['education'],item['city'],item['marital_status'],item['registered_residence'],item['language'],item['nation'],item['graduation_school'],item['hometown'],item['major'],item['zodiac'],item['religion'],item['constellation'],\
                              item['blood_type'],item['children'],item['shape'],item['self_assessment'],item['weight'],item['occupation'],item['monthly_salary'],item['company'],item['purchase'],item['company_industry'],item['car_Buying'],item['working_condition'],item['drink_status'],item['smoke_status'],item['introduce_oneself'],item['about_family'],\
                              item['requirement'].encode('utf-8'),item['life_style'],item['economic_strength'],item['hobby'],item['resource']))
        self.conn.commit()
        for url in item['url']:
            timeUUID = 'liang1' + str(uuid.uuid1())
            self.cursor.execute("insert into tbl_photo2(url,UUID,resource,r_id) values(%s,%s,%s,%s)",(url,timeUUID,item['resource'],item['ID']))
            self.conn.commit()
        return item
