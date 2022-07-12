import scrapy
from DaoMu.items import DaomuItem
from copy import deepcopy
from scrapy_redis.spiders import RedisSpider
import re
import os


class SpiderSpider(RedisSpider):

    name = 'spider1'
    # allowed_domains = ['daomubiji.com']
    # start_urls = ['http://www.daomubiji.com/']

    redis_key = 'dmbj'

    def parse(self, response):
        # 解析一级页面
        a_lis = response.xpath('//li[contains(@id,"menu-item-")]/a')
        for a in a_lis:
            item = DaomuItem()
            # 书名
            item['book_name'] = a.xpath('./text()').get()

            # 书的链接
            book_url = a.xpath('./@href').get()

            # 存放路径
            book_path = re.sub(r'[\\\/\:\*\?\"\<\>\|]', '_', item['book_name'])
            dirpath = './novel/{}'.format(book_path)

            # 创建
            if not os.path.exists(dirpath):
                os.makedirs(dirpath)

            yield scrapy.Request(book_url, callback=self.parse_second, meta={'item': deepcopy(item)})

    def parse_second(self, response):
        # 解析二级页面
        item = response.meta.get('item')
        a_lis = response.xpath('//article/a')
        for a in a_lis:
            # 章节名称
            item['chapter_title'] = a.xpath('./text()').get()
            # 章节链接
            chapter_url = a.xpath('./@href').get()
            yield scrapy.Request(chapter_url, callback=self.parse_content, meta={'item': deepcopy(item)})

    def parse_content(self, response):
        # 解析三级页面
        item = response.meta.get('item')
        content_list = response.xpath('//article[@class="article-content"]/p/text()').getall()
        item['content'] = '\n'.join(content_list)

        yield item

