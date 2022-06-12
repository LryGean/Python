import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'
}


# 获取网页源代码
def readHtml(url):
    resp = requests.get(url, headers=headers)
    resp.encoding = 'utf-8'
    html = resp.text
    resp.close()
    return html


# 解析数据
def parseHtml(html):
    soup = BeautifulSoup(html, 'html5lib')
    conmidtab = soup.select('.conMidtab')[0]
    city_tables = conmidtab.select('table')
    lst = []
    for city_div in city_tables:
        trs = city_div.select('tr')[2:]
        for tr in trs:
            dic = {}
            areas = tr.find_all('td', height="23", width="83")[0].stripped_strings
            for i in areas:
                area = i
            tem = tr.select('td[width="86"]')[0].string
            dic['城市'] = area
            lst.append(dic)
            dic['最低气温'] = tem + '°C'
    return lst


# 保存数据
def saveData(lst, name):
    head = ('城市', '最低气温')
    with open(f'./data/{name}.csv', 'w', encoding='utf-8', newline='') as f:
        csvwriter = csv.DictWriter(f, head)  # 标题
        csvwriter.writeheader()  # 写入标题
        csvwriter.writerows(lst)
        f.close()


if __name__ == '__main__':
    names = ['华北', '东北', '华东', '华中', '华南', '西北', '西南', '港澳台']
    urls = [
        'http://www.weather.com.cn/textFC/hb.shtml',
        'http://www.weather.com.cn/textFC/db.shtml',
        'http://www.weather.com.cn/textFC/hd.shtml',
        'http://www.weather.com.cn/textFC/hz.shtml',
        'http://www.weather.com.cn/textFC/hn.shtml',
        'http://www.weather.com.cn/textFC/xb.shtml',
        'http://www.weather.com.cn/textFC/xn.shtml',
        'http://www.weather.com.cn/textFC/gat.shtml'
    ]
    for i in range(len(urls)):
        html_content = readHtml(urls[i])
        # 解析数据
        ls = parseHtml(html_content)
        # 保存数据
        saveData(ls, names[i])
        print("over!")
