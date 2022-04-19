# 1.定位到2022必看片
# 2.从2022必看片中的提取到子页面的链接地址
# 3.请求子页面的链接地址， 拿到我们想要的下载地址

import requests
import re

domain = 'https://dytt89.com/'
# 网页加密解决办法verify=False
resp = requests.get(domain, verify=False)

# 指定字符集（国标：gb312或gbk）
resp.encoding = 'gb2312'

# 默认解码utf-8
# print(resp.text)

obj1 = re.compile(r"2022必看热片.*?<ul>(?P<ul>.*?)</ul>", re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)
obj3 = re.compile(r'◎片　　名.(?P<movie>.*?)<br />.*?<td '
                  r'style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">', re.S)

result1 = obj1.finditer(resp.text)

# 拿到ul里面的li
for it1 in result1:
    ul = it1.group('ul').strip()
    # print(ul)
    # 提取子页面链接：
    result2 = obj2.finditer(ul)

    child_href_list = []
    for it2 in result2:
        href = it2.group('href')
        # print(href)
        # 拼接子页面的url地址：域名 + 子页面连接
        child_href = domain + href.strip('/')
        # print(child_href)
        child_href_list.append(child_href)  # 把子页面链接保存起来

# print(child_href_list)
# 提取子页面内容
for href in child_href_list:
    child_resp = requests.get(href, verify=False)
    child_resp.encoding = 'gbk'
    # 测试
    # print(child_resp.text)
    # break
    result3 = obj3.search(child_resp.text)
    print(result3.group("movie"))
    print(result3.group("download"))
    child_resp.close()

resp.close()
