import requests
from bs4 import BeautifulSoup  # 这次项目不支持bs4解析
import csv

url = 'http://www.xinfadi.com.cn/getPriceData.html'
header = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Connection": "keep-alive",
    "Content-Length": "82",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "www.xinfadi.com.cn",
    "Origin": "http://www.xinfadi.com.cn",
    "Referer": 'http://www.xinfadi.com.cn/priceDetail.html',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}
s = input("请输入页数：")
data = {
    "limit": "",
    "current": s
}

resp = requests.post(url, headers=header, data=data)
f = open("./Data/菜价.csv", "w", encoding="utf-8")
csvwriter = csv.writer(f)

# print(resp.text)
# print(resp.json())

r = resp.json()
# print(r["list"])
li = r["list"]

# 解析数据
# 1.把页面源代码交给BeautifulSoup进行处理，生成bs对象
# 注意："html.parser"——>指定html解析器
# page = BeautifulSoup(resp.text, "html.parser")

# 2.从bs对象中查找数据
# find(标签，属性值='')：只找第一个指定对象
# 对于python中的关键字做属性，需加下划线
# 例子:page.find("table", class_="...")
# 等价写法：page.find("table", attrs={"class":"..."})
# find_all(标签，属性值='')：找全部指定对象

for i in li:
    # print(i.values())
    # print(i['prodName'], i['lowPrice'], i['highPrice'], i['avgPrice'],
    #       i['place'], i['specInfo'], i['unitInfo'], i['pubDate'])
    csvwriter.writerow([i['prodName'], i['lowPrice'], i['highPrice'], i['avgPrice'], i['place'], i['specInfo'],
                        i['unitInfo'], i['pubDate']])
print("over!")
f.close()
resp.close()
