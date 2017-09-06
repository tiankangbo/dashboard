# -*- coding:utf-8 -*-
import csv
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class CSV(object):
    #初始化两个参数，csv_name文件路径+文件名，另一个是第一行每一列的字段名
    def __init__(self, csv_name, firstRow=[]):
        self.name = csv_name
        #判断.csv文件是否存在，存在退出程序，然后需要在主代码更换文件名
        #这一块后续可以改进
        if os.path.exists(csv_name):
            print '文件已存在，请更换文件名'
            os._exit(1)
        with open(self.name, "ab+") as files:
            write = csv.writer(files)
            write.writerow(firstRow)
    #row写入行每一列的数据
    def writeRow(self,row=[]):
        with open(self.name, "ab+") as files:
            write = csv.writer(files)
            write.writerow(row)
