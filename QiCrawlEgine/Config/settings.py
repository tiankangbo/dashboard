# coding:utf8
"""
-------------------------------------------------
   File Name：     settings.py
   Description :  配置文件
   Author :       tiankangbo
   date：         2017/10/16
-------------------------------------------------
   Change Activity:
-------------------------------------------------
"""
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

'''mini 监控的主机配置文件，即ip， 监听端口'''
host_settings = {
    # "HOST": '192.168.20.148',
    "HOST": '127.0.0.1',
    "PORT": 8888
}

'''数据库信息, mongoDB, mysql'''
db_settings = {
    "mongodb_ip": '127.0.0.1',
    "mongodb_port": 27017,
    "mysql_ip": '127.0.0.1',
    # "mysql_ip": '192.168.10.24',
    "mysql_port": 3306,
    "mysql_user": 'root',
    "mysql_passwd": 'pa$$w0rd',
    # "mysql_passwd": '123456',
    "mysql_db": 'QicrawlDB',
    "mysql_table": 'spiderinfo'
}

'''每次迭代添加新的爬虫模板需要在此注册  '模板名':'爬虫函数.类名字()'    '''
template_settings = {
    '虎嗅网': 'huxiu.HuXiu',
    '智联招聘': 'zhilian.ZhiLian',
    '小猪短租': 'xiaozhu.XiaoZhu',
    '爱壁纸': 'aibizhi.Love_bg_image',
    '蚂蚁短租': 'mayi.MaYi',
    '前程无忧': 'qiancheng.QianCheng'
}

'''爬虫的请求header'''
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'
}
