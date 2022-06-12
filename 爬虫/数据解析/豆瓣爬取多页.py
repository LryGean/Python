import requests
from lxml import etree
import csv

# url = 'https://movie.douban.com/top250?start=0&filter='

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}


# 获取网页源码
def readPage(url):
    resp = requests.get(url, headers=header)
    html = resp.text
    return html


# 解析数据
def parseHtml(html):
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
        dic['title'] = ''.join(title + other_title)
        dic['url'] = link[0]
        dic['star'] = star[0]
        dic['quote'] = quote
        lst.append(dic)
    return lst


def saveDate(lst, page):
    with open(f'./data/douban{page}.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['title', 'url', 'star', 'quote'])
        writer.writeheader()
        writer.writerows(lst)


for i in range(1, 11):
    url = f'https://movie.douban.com/top250?start={(i-1)*25}&filter='
    html = readPage(url)
    # 解析数据
    lst = parseHtml(html)
    # 保存数据
    saveDate(lst, i)
