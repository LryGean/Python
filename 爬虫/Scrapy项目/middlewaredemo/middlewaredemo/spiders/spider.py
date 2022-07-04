# 中间件
# 应用：修改user-Agent

import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['www.httpbin.org']
    start_urls = ['https://www.httpbin.org/get']

    def start_requests(self):
        for i in range(5):
            url = f"{self.start_urls[0]}?query={i}"
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        # print('解析方法')
        print(response.text)
        # print(response.status)
