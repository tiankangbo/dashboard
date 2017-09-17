# coding:utf8
"""
-------------------------------------------------
   File Name：     send_main.py
   Description :  发送预警邮件
   Author :       tiankangbo
   date：         2017/3/13
-------------------------------------------------
   Change Activity:
-------------------------------------------------
"""

import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import smtplib
import warn.readjson
from email.mime.text import MIMEText
from email.utils import formataddr

#from realtidt import cpu_stat

'''发件人的邮箱帐号'''
#sender = 'kangbotian@163.com'
#sender = warn.readjson.usage_command("sender")
#sender_name = warn.readjson.usage_command("sender_name")
'''收件人的邮箱帐号'''
#user = 'sun.kangbo@foxmail.com'
#user = warn.readjson.usage_command("user")
'''警告信息'''
#warning = 'CPU预警'

def send_mail(warning):
    ret = True
    try:
        msg = MIMEText(warning, 'plain', 'utf-8')

        '''对应发件人邮箱昵称，发件人邮箱帐号'''
        msg['From'] = formataddr([warn.readjson.usage_command("sender_name"), warn.readjson.usage_command("sender_address")])

        '''对应收件人邮箱昵称，邮箱帐号'''
        msg['To'] = formataddr([warn.readjson.usage_command("user_nickname"), warn.readjson.usage_command("user_address")])
        '''标题'''
        msg['Subject'] = "主题"

        '''发件人邮箱的SMTP服务器, smtp默认端口25'''
        server = smtplib.SMTP(warn.readjson.usage_command("SMTP_server"), 25)

        '''对应发件人的邮箱帐号，以及第三方登录授权密码，此处163的授权密码需要登录163邮箱官网进行配置，打开smtp服务'''
        server.login(warn.readjson.usage_command("sender_address"), warn.readjson.usage_command("sender_key"))

        '''对应发件人的邮箱帐号，收件人的邮箱帐号，以及发送的邮件'''
        server.sendmail(warn.readjson.usage_command("sender_address"), [warn.readjson.usage_command("user_address"), ], msg.as_string())

        '''关闭与服务器链接'''
        server.quit()

    except Exception, e:
        print e
        ret = False

    return ret

if __name__ == '__main__':

    print send_mail('cpu预警')