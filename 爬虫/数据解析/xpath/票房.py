import requests
import lxml
import csv
from lxml import etree

url = 'http://www.piaofang.biz/'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}

resp = requests.get(url, headers=headers)

html = etree.HTML(resp.content)

trs = html.xpath('//table/tr/td[@class="title"]')

lst = []
for tr in trs:
    item = {}
    movieText = tr.xpath('./a/text()')
    if not movieText:
        item['电影名'] = tr.xpath('./text()')[0].strip("《").strip("》")
    else:
        item['电影名'] = movieText[0]
    item['票房'] = "".join(tr.xpath('../td[@class="piaofang"]//text()'))
    # print(item)
    lst.append(item)

with open("./Data/票房csv", 'w', encoding="utf-8", newline="") as f:
    th = ('电影名', '票房')
    csvwriter = csv.DictWriter(f, th)
    csvwriter.writeheader()
    csvwriter.writerows(lst)
    print("over!")
    f.close()
