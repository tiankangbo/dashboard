# coding=utf-8
# @author:liang
# @time :20170709


import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


class AutoMail():

    mail_user = "sincerely90@163.com"  #用户名
    mail_passwed = "dasdasdasda"  # 密码

    def send_mail(self, theme, detail, post=''):
        if post:
            self.post = post
        else:
            self.post = '946439674@qq.com'
        try:
            msg = MIMEText(detail, 'plain', 'utf-8')
            msg['From'] = formataddr(["loading_miracles", self.mail_user])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To'] = formataddr(["liang", self.post])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = theme  # 邮件的主题，也可以说是标题
            server = smtplib.SMTP_SSL("smtp.163.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
            server.login(self.mail_user, self.mail_passwed)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(self.mail_user, [self.post, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()
            print('send successfully:', self.post)
        except Exception:
            print("send failed:",self.post)
