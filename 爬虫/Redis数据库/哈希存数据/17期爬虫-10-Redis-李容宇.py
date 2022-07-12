# 9.(必做题1)：读取douban_data.csv文件写入redis
# 需求：
# 1. 把rank作为键
# 2. value应该包含title,rating_num,comment_num,quote字段
# 3. 获取键为99，对应的电影名称

# https://www.yuque.com/docs/share/661d848d-ce89-4b76-bb9c-34287d757a4f?#

import csv
import redis
class DouBanSpider:
    def __init__(self):
        self.conn = redis.StrictRedis(host='127.0.0.1', port=6379, db=0, decode_responses=True)

    def read_csv(self):
        with open('./data/douban_data.csv', 'r', encoding='utf-8') as f:
            csvreader = csv.DictReader(f)
            for i in csvreader:
                value = {k: v for k, v in i.items() if k in ['title', 'rating_num', 'comment_num', 'quote']}
                self.string_hmset(i['rank'], value)
                self.string_hvals(i['rank'])

    def string_hmset(self, k, y):
        # 写入
        self.conn.hmset(k, y)

    def string_hvals(self, k):
        # 读取
        res = self.conn.hvals(k)
        print(res)

    def run(self):
        self.read_csv()


if __name__ == '__main__':
    s = DouBanSpider()
    s.run()

