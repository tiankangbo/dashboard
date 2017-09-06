# coding:utf8
__author__ = 'tiankangbo'

'''构造request headers'''
import re
import requests


def get_xsrf(session):
    # _xsrf 是一个动态的数据，可以从网页中进行匹配
    index_url = 'http://www.zhihu.com'
    # 获取登录的时候需要的_xsrf, 是防止跨站请求伪造的
    index_page = session.get(index_url, headers=headers)
    html = index_page.text

    pattern = r'name="_xsrf" value="(.*?)"'

    # 这里的_xsrf返回的是一个列表
    _xsrf = re.findall(pattern, html)
    print("_xsrf", _xsrf)
    return _xsrf[0]

# agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0'
agent = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Mobile Safari/537.36'

# agent = 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
headers = {
    'User-Agent':agent
}

session = requests.session()
_xsrf = get_xsrf(session)

post_url = 'https://www.zhihu.com/login/phone_num'
postdata = {
    '_xsrf': _xsrf,
    'password':'nylg1415925605',
    'remember_me':'true',
    'phone_num':'15503772716'
}

login_page = session.post(post_url, data=postdata, headers=headers)
login_code = login_page.text

print(login_page.status_code)
# print(login_code)
