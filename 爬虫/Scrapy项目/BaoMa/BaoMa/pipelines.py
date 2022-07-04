# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import random

import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import requests


class BaomaPipeline(ImagesPipeline):
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

    # # 下载方法一成功获取1927张：
    # def process_item(self, item, spider):
    #     resp = requests.get(item['url'], headers=random.choice(self.headers))
    #     with open(f'./car/{item["car_name"]}.jpg', 'wb') as f:
    #         f.write(resp.content)
    #         f.close()
    #         resp.close()
    #     return item

    # 下载方法二：
    def get_media_requests(self, item, info):
        image_url = item['url']
        # print(image_url)
        yield scrapy.Request(image_url, headers=random.choice(self.headers))

    def file_path(self, request, response=None, info=None, *, item=None):
        name = item['car_name']
        return f'full/{name}.jpg'

    # # 可以将item 传递给下一个即将被执行的管道类
    # def item_completed(self, results, item, info):
    #     print(item['car_name'])
    #     return item
