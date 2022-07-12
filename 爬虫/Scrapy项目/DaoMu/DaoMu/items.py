# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DaomuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 1. 书的名字
    book_name = scrapy.Field()
    # 2. 章节名称
    chapter_title = scrapy.Field()
    # 3. 文本内容
    content = scrapy.Field()

