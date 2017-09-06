# coding:utf8
__author__ = 'tiankangbo'

import requests
import time
import re
from PIL import Image


#
agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'
headers = {
    "Host": "www.zhihu.com",
    "Referer": "https://www.zhihu.com/",
    'User-Agent': agent
}

########### 开始登陆
def get_xsrf(session):
    # _xsrf 是一个动态的数据，可以从网页中进行匹配
    index_url = 'http://www.zhihu.com'
    # 获取登录的时候需要的_xsrf, 是防止跨站请求伪造的
    index_page = session.get(index_url, headers=headers)
    html = index_page.text
    pattern = r'name="_xsrf" value="(.*?)"'
    # 这里的_xsrf返回的是一个列表
    _xsrf = re.findall(pattern, html)
    return _xsrf[0]

session = requests.session()
xsrf_token = get_xsrf(session)

headers['X-Xsrftoken'] = xsrf_token
headers['X-Requested-With'] = 'XMLHttpRequest'
loginurl = 'https://www.zhihu.com/login/email'

postdata = {
    '_xsrf': xsrf_token,
    'email': 'tiankangbo@gmail.com',
    'password': 'nylg1415925605'
}

loginresponse = session.post(url=loginurl, headers=headers, data=postdata)
# print('服务器端返回响应码：', loginresponse.status_code)
print(loginresponse.json())

# 验证码问题输入导致失败: 猜测这个问题是由于session中对于验证码的请求过期导致
if loginresponse.json()['r']==1:

    randomtime = str(int(time.time() * 1000))
    captchaurl = 'https://www.zhihu.com/captcha.gif?r=' + randomtime + "&type=login"
    captcharesponse = session.get(url=captchaurl, headers=headers)
    with open('checkcode.gif', 'wb') as f:
        f.write(captcharesponse.content)
        f.close()

    im = Image.open('checkcode.gif')
    im.show()
    im.close()
    # os.startfile('checkcode.gif')
    # os.open('checkcode.gif')
    captcha = input('请输入验证码：')
    print(captcha)

    postdata['captcha'] = captcha
    loginresponse = session.post(url=loginurl, headers=headers, data=postdata)
    print('服务器端返回响应码：', loginresponse.status_code)
    print(loginresponse.json())


