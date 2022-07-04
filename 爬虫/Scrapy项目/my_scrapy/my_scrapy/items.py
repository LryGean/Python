# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# 定义数据采集字段
class MyScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    # 名言
    text = scrapy.Field()
    # 名人
    author = scrapy.Field()
    # 标签
    tags = scrapy.Field()
