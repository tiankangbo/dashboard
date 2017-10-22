import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'
}

category = {
    '影视明星': '1',
    '风光风景': '2',
    '花卉植物': '4',
    '魅力女性': '3',
    '游戏CG': '6',
    '动物宠物': '5',
    '卡通动漫': '7',
    '机车世界': '798',
    '炫彩美图': '2098',
    '品牌欣赏': '10',
    '美食天下': '1546',
    '影视剧集': '797',
    '美丽文字': '21866',
    '体育运动': '1554',
    '艺术设计': '1407',
    '节庆假日': '8',
    '军事战争': '2180',
    '美图杂烩': '2097'
}


class Love_bg_image(object):
    # 分类总URL
    url = "http://api.lovebizhi.com/windows_v3.php?a=category&spdy=1&device=&uuid=10a577628ff8444580615ead9ce04f50&mode=0&client_id=1004&device_id=75347347&model_id=106&size_id=0&channel_id=30001&screen_width=1366&screen_height=768&bizhi_width=1366&bizhi_height=768&version_code=33&language=zh-CN&mac=&p=1&tid={}"

    # get请求  获取json
    def get_r_request(self):
        html = requests.get(self.url, headers=headers).json()
        return html

    # 下载图片
    def store(self, url):
        img = requests.get(url, headers=headers)
        yield img

    # 获取图片列表
    def detail(self, html):
        for pic in html['data']:
            url = pic['image']['diy']
            yield self.store(url)

            # 入口  参数 类别

    def run(self, cate):
        self.url = self.url.format(category[cate])
        test = self.detail(self.get_r_request())
        for one in test:
            for on in one:
                try:
                    with open('/root/PycharmProjects/QiCrawlEgine/Spiders/Image/{}'.format(on.url.split('/')[-1]), 'wb') as f:
                        f.write(on.content)
                    f.close()
                    yield {'图片类别': cate, '图片名字': on.url.split('/')[-1], '图片URL': on.url, '状态': '已下载'}

                except:
                    yield {'图片类别': cate, '图片名字': on.url.split('/')[-1], '图片URL': on.url, '状态': '下载失败'}


if __name__ == "__main__":
    love = Love_bg_image()
    love.run("影视明星")