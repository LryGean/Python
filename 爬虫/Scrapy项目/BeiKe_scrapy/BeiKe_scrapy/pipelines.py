# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv

from itemadapter import ItemAdapter


class BeikeScrapyPipeline:
    def __init__(self):
        self.writer = csv.writer(open('./BeiKe_scrapy/Data/贝壳找房.csv', 'w+', encoding='utf-8', newline=''))
        self.headers = ('title', 'region', 'block', 'community', 'area', 'toward', 'type', 'rent', 'time')
        self.writer.writerow(self.headers)

    def process_item(self, item, spider):
        rows = []
        for header in self.headers:
            rows.append(item[header])
        rows = tuple(rows)
        self.writer.writerow(rows)
        print("Over！")
        return item

    def close_spider(self, spider):
        print('关闭文件')
        self.f.close()
