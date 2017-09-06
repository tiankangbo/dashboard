import requests
from lxml import etree
import time

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'
}
def getTime(url):
    html = requests.get(url, headers=headers)
    # print(html.text)
    data = etree.HTML(html.text)
    time = data.xpath('//div[@class="column-link-box"]/span[1]/text()')[0]
    print(time)

def getHot(url):
    html = requests.get(url,headers=headers)
    # print(html.text)
    data = etree.HTML(html.text)
    hots = data.xpath('//div[@class="mob-ctt"]')
    #print(hots)
    for hot in hots:
        print(hot.xpath('h2/a/text()')[0])
        getTime('https://www.huxiu.com'+hot.xpath('h2/a/@href')[0])

def getAjax(url, page):
    data = {
        'huxiu_hash_code':'346a1b4f50149b17f0cd018c57ce0b90',
        'page':page,
        'last_dateline':'1503135360'
    }
    html = requests.post(url, headers=headers, data=data)
    data = html.json()
    data = etree.HTML(data['data'])
    hots = data.xpath('//div[@class="mob-ctt"]')
    for hot in hots:
        print(hot.xpath('h2/a/text()')[0])
    #     getTime('https://www.huxiu.com'+hot.xpath('h2/a/@href')[0])

def getall():
    url = 'https://www.huxiu.com/v2_action/article_list'
    for page in range(2, 30):
        getAjax(url=url, page=page)
        time.sleep(1)

if __name__ == "__main__":
    # getHot('https://www.huxiu.com/channel/106.html')
   # 'https://www.huxiu.com/channel/ajaxGetMore'
   #  'https://www.huxiu.com/v2_action/article_list'
   #  getAjax('https://www.huxiu.com/channel/ajaxGetMore')
   getall()