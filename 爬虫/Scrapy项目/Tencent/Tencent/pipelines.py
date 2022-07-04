# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv


class TencentPipeline:
    # f = open('./Data/tencent.csv', 'w+', encoding='utf-8-sig', newline='')
    # w = csv.DictWriter(f, fieldnames=['job_name', 'job_duty'])
    # w.writeheader
    def __init__(self):
        self.writer = csv.writer(open('./Data/tencent.csv', 'w+', encoding='utf-8-sig', newline=''))
        self.headers = ('job_name', 'job_duty')
        self.writer.writerow(self.headers)

    def process_item(self, item, spider):
        rows = []
        for header in self.headers:
            rows.append(item[header])
        rows = tuple(rows)
        self.writer.writerow(rows)
        print("Over！")
        return item
