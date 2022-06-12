import requests
import re
import csv

url = 'http://www.weather.com.cn/weather/101250101.shtml'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'
}

# 匹配ul数据：.*(<ul class="t clearfix">.*?</ul>)
# 匹配li数据：findall('<li.*?>.*?</li>')
# 遍历：
# <li.*?>.*?
# <h1>(.*?)</h1>.*?
# <p.*?>(.*?)</p>
# .*?<i>(.*?)</i>
# .*?
# <i>(.*?)</i>
# .*?
# </li>

resp = requests.get(url, headers=headers)
resp.encoding = "utf-8"
# 获取原码
content = resp.text

# 匹配ul
ul = re.match('.*(<ul class="t clearfix">.*?</ul>)', content, re.S)
ul = ul.group(1)  # 拿到ul的数据
# 获取所有li
lis = re.findall('<li.*?>.*?</li>', ul, re.S)
# print(lis)
pattern = re.compile('''<li.*?>.*?<h1>(.*?)</h1>.*?<p.*?>(.*?)</p>.*?<i>(.*?)</i>.*?<i>(.*?)</i>.*?</li>''', re.S)
lst = []
for li in lis:
    r = pattern.match(li)
    lis_one = [r.group(1), r.group(2), r.group(3), r.group(4)]
    lst.append(lis_one)
header = ('日期', '天气', '气温', '风力')
with open('weather.csv', 'w', encoding='utf-8', newline='') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(lst)
