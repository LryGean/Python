import time
import requests
from lxml import etree
import csv


# 获取网页源代码
def readHtml(ur, headers):
    resp = requests.get(ur, headers=headers)
    resp.encoding = "gbk"
    html = resp.text
    # print(html)
    return html


# 解析数据
def parseHtml(html, headers):
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
        res = requests.get(href, headers=headers)
        res.encoding = 'gbk'
        htmltext = res.text
        htm = etree.HTML(htmltext)
        content = htm.xpath('//div[@id="content"]/text()')
        # print(content)
        save_data(content, title)
        lst.append(dic)
    return lst


def saveDate(lst):
    with open('./Data/笔趣阁.csv', 'w', encoding="utf-8", newline='') as f:
        th = ('标题', '链接')
        csvwriter = csv.DictWriter(f, th)
        csvwriter.writeheader()
        csvwriter.writerows(lst)


# 保存数据
def save_data(content, title):
    with open(f'./book/{title}.txt', 'w', encoding='utf-8', newline='') as f:
        f.writelines(content)  # 写入多行


def main():
    # 第一部：url
    url = 'https://www.qbiqu.com/0_305/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
    }
    html1 = readHtml(url, headers)
    # 保存数据
    lst = parseHtml(html1, headers)
    saveDate(lst)


if __name__ == '__main__':
    t1 = time.time()
    main()
    t2 = time.time()
    print(t2-t1)
