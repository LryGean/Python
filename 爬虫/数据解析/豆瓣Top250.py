# 需求：爬取标题，评分，引言，详情页url
import requests
from lxml import etree
import csv

# page = input("请输入页数")
url = 'https://movie.douban.com/top250?start=0&filter='

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}

# div[@class="info"]
# 主标题：div[@class="hd"]/a/span[@clas="title"]/text()
# 副标题：div[@class="hd"]/a/span[@clas="other"]/text()

# 详情页url:div[@class="hd"]/a/@href
# 评分div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()
# 引言:div[@class="bd"]/p[@class="quote"]/span/text()

resp = requests.get(url, headers=header)
html = resp.text
# print(html)

html_element = etree.HTML(html)

movielist = html_element.xpath('//div[@class="info"]')  # 列表
# print(movielist)
lst = []
# //*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span[1]
for movie in movielist:
    dic = {}
    title = movie.xpath('.//div[@class="hd"]/a/span[@class="title"]/text()')
    other_title = movie.xpath('.//div[@class="hd"]/a/span[@class="other"]/text()')
    link = movie.xpath('.//div[@class="hd"]/a/@href')
    star = movie.xpath('.//div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()')
    quote = movie.xpath('.//div[@class="bd"]/p[@class="quote"]/span/text()')
    dic['title'] = ''.join(title+other_title)
    dic['url'] = link
    dic['star'] = star
    dic['quote'] = quote
    lst.append(dic)

with open('douban.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['title', 'url', 'star', 'quote'])
    writer.writeheader()
    writer.writerows(lst)




