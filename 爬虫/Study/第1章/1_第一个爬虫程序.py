# 爬虫：通过编写程序来获取互联网上的资源
# 百度
# 需求：用程序模拟浏览器，输入一个网址，从该网址中获取到资源或者内容
from urllib.request import urlopen

# 打开网址
url = "http://www.baidu.com"
# 得到响应
resp = urlopen(url)

# 读取内容
r = resp.read()
# print(r.decode("utf-8"))

with open("baidu.html", "w", encoding="utf-8") as f:
    f.write(r.decode("utf-8"))     # 读取网页源代码
print("over!")

f.close()
