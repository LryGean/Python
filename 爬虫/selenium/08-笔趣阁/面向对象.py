import time
import requests
from lxml import etree
import csv


class Book_Store:
    def __init__(self):
        # 第一部：url
        self.url = 'https://www.qbiqu.com/0_305/'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
        }

    def readHtml(self):
        resp = requests.get(self.url, headers=self.headers)
        resp.encoding = "gbk"
        html = resp.text
        # print(html)
        return html

    def parseHtml(self, html):
        html_element = etree.HTML(html)
        lis = html_element.xpath('//div[@id="list"]/dl/dd')[9:]
        # print(lis)
        lst = []
        for i in lis:
            dic = {}
            title = i.xpath('.//a/text()')[0]
            href = 'https://www.qbiqu.com' + i.xpath('.//a/@href')[0]
            # print(title, href)
            dic['标题'] = title
            dic['链接'] = href
            res = requests.get(href, headers=self.headers)
            res.encoding = 'gbk'
            htmltext = res.text
            htm = etree.HTML(htmltext)
            content = htm.xpath('//div[@id="content"]/text()')
            # print(content)
            self.save_data(content, title)
            lst.append(dic)
        return lst

    def saveDate(self, lst):
        with open('./Data/笔趣阁.csv', 'w', encoding="utf-8", newline='') as f:
            th = ('标题', '链接')
            csvwriter = csv.DictWriter(f, th)
            csvwriter.writeheader()
            csvwriter.writerows(lst)

    # 保存数据
    def save_data(self, content, title):
        with open(f'./book/{title}.txt', 'w', encoding='utf-8', newline='') as f:
            f.writelines(content)  # 写入多行

    def main(self):
        html = self.readHtml()
        lst = self.parseHtml(html)
        self.saveDate(lst)


if __name__ == '__main__':
    t1 = time.time()
    zs = Book_Store()
    zs.main()
    t2 = time.time()
    print(t2-t1)
