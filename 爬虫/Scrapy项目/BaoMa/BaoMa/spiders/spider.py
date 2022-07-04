# 7.(必做题1)目标网站：汽车之家
# 示例网址：https://www.autohome.com.cn/65/#levelsource=000000000_0&pvareaid=101594
# 需求：
# 1. 使用scrapy框架爬取该汽车的实拍图片
# 2. 保存图片到car文件夹
# 3. 图片数量不得少于500张

import random

import scrapy

from BaoMa.items import BaomaItem


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['www.autohome.com']
    start_urls = ['https://www.autohome.com.cn/65/#levelsource=000000000_0&pvareaid=101594']

    headers = [
        {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'},
        {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'},
        {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36'},
        {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.0.0 Safari/537.36'}
    ]

    # def start_requests(self):
    #     # 构造请求(随机)
    #     yield scrapy.Request(url=self.start_urls[0], callback=self.parse, headers=random.choice(self.headerds))

    def parse(self, response):
        url = response.xpath('//div[@id="navTop"]/ul/li[3]/a/@href').get()
        url = response.urljoin(url)
        yield scrapy.Request(url=url, callback=self.parse_real_pic,
                             headers=random.choice(self.headers), dont_filter=True)

    def parse_real_pic(self, response):
        uibox_title = response.xpath('//div[@class="uibox"]/div[@class="uibox-title"]/a[1]')
        for i in range(len(uibox_title)):
            url = uibox_title[i].xpath('.//@href').get()
            name = uibox_title[i].xpath('.//text()').get()
            title_url = response.urljoin(url)
            if i == 0:
                yield scrapy.Request(title_url, headers=random.choice(self.headers),
                                     callback=self.first_url, cb_kwargs={'name': name},
                                     dont_filter=True)
            else:
                yield scrapy.Request(title_url, headers=random.choice(self.headers),
                                     callback=self.other_url, cb_kwargs={'name': name},
                                     dont_filter=True)

    # 全景看车：16张图
    def first_url(self, response, name):
        # print(response.text)
        lis = response.xpath('//ul[@class="content-detail"]/li')
        for i in range(len(lis)):
            item = BaomaItem()
            item['url'] = lis[i].xpath('.//img/@src').get()
            car_name = lis[i].xpath('.//p/text()').getall()
            car_name = name + '_' + '_'.join(car_name).replace(' ', '_') + f'_{i+1}'
            item['car_name'] = car_name
            yield item

    # 车身外观：84张
    # 中控方向盘：462张
    # 车厢座椅：471张
    # 其他细节：729张
    # 改装：165张
    def other_url(self, response, name):
        # 判断当前第几页
        next_url = response.xpath('//div[@class="page"]/a[last()]/@href').get()
        # 判断首页
        if next_url.split('-')[-1] == 'p2.html':
            num = 1
        else:
            num = int(response.url.split('-p')[-1].strip('.html'))
        print(f'{name}当前第{num}页')
        lis = response.xpath('//div[@class="uibox-con carpic-list03 border-b-solid"]/ul/li')
        print(f'获取：{len(lis)}')
        for i in range(len(lis)):
            item = BaomaItem()
            car_message = lis[i].xpath('.//div/a/text()').get()
            item['car_name'] = name + '_' + car_message.replace(' ', '_') + f'_{60*(num-1) + i + 1}'
            url = f"https:{lis[i].xpath('.//img/@src').get()}"
            item['url'] = url
            yield item
            # print(item)

        # 翻页
        if next_url != 'javascript:void(0);':
            url = response.urljoin(next_url)
            # print(url)
            yield scrapy.Request(url=url, callback=self.other_url,
                                 headers=random.choice(self.headers),
                                 cb_kwargs={'name': name}, dont_filter=True)
