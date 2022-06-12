import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import csv

url = 'http://www.weather.com.cn/textFC/gat.shtml'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'
}


resp = requests.get(url, headers=headers)
resp.encoding = 'utf-8'
html = resp.text

soup = BeautifulSoup(html, 'lxml')
hanml = soup.select('.hanml')[0]
conMidtabs = soup.select('.conMidtab')
# print(len(conMidtabs))
conMidtabs_list = []
for conMidtab in conMidtabs:
    if len(conMidtab.attrs) == 1:
        conMidtabs_list.append(conMidtab)

for conMidtab in conMidtabs_list:
    tables = conMidtab.select('table')[0:3]
lst = []
for table in tables:
    trs = table.select('tr')[2:]
    for tr in trs:
        dic = {}
        areas = tr.find_all('td', height="23", width="83")[0].stripped_strings
        for i in areas:
            area = i
        tem = tr.select('td[width="86"]')[0].string
        dic['城市'] = area
        dic['最低气温'] = tem + '°C'
        lst.append(dic)
print(lst)

# head = ('城市', '最低气温')
# with open('./csv/lowWeather.csv', 'w', encoding='utf-8', newline='') as f:
#     csvwriter = csv.DictWriter(f, head)  # 标题
#     csvwriter.writeheader()  # 写入标题
#     csvwriter.writerows(lst)
#     f.close()
#     print("over!")


# lst = []
# for city_div in city_divs:
#     trs = city_div.select('tr')[2:]
#     for tr in trs:
#         dic = {}
#         areas = tr.find_all('td', height="23", width="83")[0].stripped_strings
#         for i in areas:
#             area = i
#         tem = tr.select('td[width="86"]')[0].string
#         dic['城市'] = area
#         dic['最低气温'] = tem + '°C'
#         lst.append(dic)
#
#
# head = ('城市', '最低气温')
# with open('./csv/lowWeather.csv', 'w', encoding='utf-8', newline='') as f:
#     csvwriter = csv.DictWriter(f, head)  # 标题
#     csvwriter.writeheader()  # 写入标题
#     csvwriter.writerows(lst)
#     f.close()
#     print("over!")


