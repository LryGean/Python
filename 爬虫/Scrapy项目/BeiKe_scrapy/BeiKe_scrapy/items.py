# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BeikeScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 房源标题
    title = scrapy.Field()
    # 所在区域
    region = scrapy.Field()
    # 所在街区
    block = scrapy.Field()
    # 社区
    community = scrapy.Field()
    # 房间面积
    area = scrapy.Field()
    # 朝向
    toward = scrapy.Field()
    # 类型
    type = scrapy.Field()
    # 租金
    rent = scrapy.Field()
    # 时间
    time = scrapy.Field()
