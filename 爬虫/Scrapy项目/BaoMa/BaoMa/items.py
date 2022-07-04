# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BaomaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 图片名称
    car_name = scrapy.Field()
    # 图片地址
    url = scrapy.Field()
