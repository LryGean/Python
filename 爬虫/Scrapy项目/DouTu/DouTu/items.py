# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoutuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 图片名称
    img_name = scrapy.Field()
    # 图片链接
    img_url = scrapy.Field()
