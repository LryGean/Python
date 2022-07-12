# Define your item pipelines heres
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re

class DaomuPipeline:
    def process_item(self, item, spider):
        filename = './novel/{}/{}.text'.format(
            re.sub(r'[\\\/\:\*\?\"\<\>\|]', '_', item['book_name']),
            re.sub(r'[\\\/\:\*\?\"\<\>\|]', '_', item['chapter_title'])
        )
        print(f'正在写入{item["chapter_title"]}')

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(item['content'])

        return item
