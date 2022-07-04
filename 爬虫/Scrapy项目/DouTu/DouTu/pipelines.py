# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline


class DoutuPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        img_url = item['img_url']
        yield scrapy.Request(img_url)

    def file_path(self, request, response=None, info=None, *, item=None):
        name = item['img_name']
        return f'{name}.gif'

