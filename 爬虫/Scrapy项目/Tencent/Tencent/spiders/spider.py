import json

import scrapy

from Tencent.items import TencentItem


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['tencent.com']
    first_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1655991442875&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
    second_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1655991540289&postId={}&language=zh-cn'
    start_urls = [first_url.format(1)]

    def parse(self, response):
        data = json.loads(response.text)

        for job in data['Data']['Posts']:
            item = TencentItem()
            item['job_name'] = job['RecruitPostName']
            post_id = job['PostId']
            # print(item['job_name'])

            detail_url = self.second_url.format(post_id)

            # 构造请求
            yield scrapy.Request(url=detail_url, callback=self.parse_detail, meta={'item': item})

        # 翻页
        for page in range(2, 11):
            url = self.first_url.format(page)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse_detail(self, response):
        # 解析详情页数据内容
        item = response.meta.get('item')
        data = response.json()
        item['job_duty'] = data['Data']['Requirement']
        # print(item['job_duty'])
        yield item
