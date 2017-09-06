
import requests

url = 'http://192.168.25.191/qitech/login'
# url = 'https://www.zhihu.com/settings/profile'

response = requests.get(url,auth=('admin','admin'))

print("服务器返回状态 -- " , response.status_code)
print("response header -- ", response.headers)
print("cookies -- ", response.cookies)
print("history -- ", response.history)
print(response)
