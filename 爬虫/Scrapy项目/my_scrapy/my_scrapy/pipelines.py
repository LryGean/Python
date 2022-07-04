# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from my_scrapy.settings import MONGODB_DATABASE


# 数据保存
class MyScrapyPipeline:
    def process_item(self, item, spider):
        with open('demo.txt', 'a', encoding='utf-8') as f:
            f.write(item['text'] + '\n')

        return item


# 保存到MongoDB里
class MongoDBPipeline:
    def __init__(self):
        self.conn = pymongo.MongoClient()
        self.db = self.conn[self.database]
        self.database = MONGODB_DATABASE

    @classmethod
    def from_crawler(cls, crawler):
        # 获取全局配置项
        cls.database = crawler.settings.get('MONGODB_DATABASE')
        return cls

    def open_spider(self, spider):
        print('开启连接')
        # 开启爬虫调用
        self.conn = pymongo.MongoClient()
        # self.db = self.conn['demo']
        self.db = self.conn[self.database]

    def process_item(self, item, spider):
        self.db['my_demo1'].insert_one(dict(item))
        return item

    def close_spider(self, spider):
        # 结束爬虫调用
        self.conn.close()
        print('关闭连接')
