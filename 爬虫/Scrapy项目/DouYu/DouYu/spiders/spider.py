import scrapy
from DouYu.items import DouyuItem
import json

class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['douyu.com']
    url = 'https://m.douyu.com/api/room/list?page={}&type=yz'
    offset = 1

    start_urls = [url.format(offset)]

    def parse(self, response):
        datas = json.loads(response.text)['data']['list']
        for data in datas:
            item = DouyuItem()
            item['nickname'] = data['nickname']
            item['verticalSrc'] = data['verticalSrc']

            yield item

        self.offset += 1
        if self.offset <= 5:
            yield scrapy.Request(self.url.format(self.offset), callback=self.parse)
