# 拿到页面源代码   request
# 通过re来提取想要的有效信息   re
import requests
import re
import csv

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"
}

# ************************
# 多个模式用 | 隔开         *
# re.I:忽略大小写匹配       *
# re.S：表示可以包含\n的匹配 *
# ************************

# 解析数据
# .*?惰性匹配
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                 r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp;.*?<span '
                 r'class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                 r'<span>(?P<num>.*?)</span>', re.S)

page = 1
for i in range(0, 250, 25):
    url = f'https://movie.douban.com/top250?start={i}&filter='
    resp = requests.get(url, headers=header)
    # 页面源代码
    page_content = resp.text
    # print(resp.text)
    # 开始匹配
    result = obj.finditer(page_content)
    f = open(f"./Data/第{page}页.scv", "w", encoding="utf-8")
    csvwriter = csv.writer(f)

    for it in result:
        # print(it.group("name"))
        # print(it.group("year").strip())
        # print(it.group("score"))
        # print(it.group("num"))
        dic = it.groupdict()
        dic['year'] = dic['year'].strip()
        csvwriter.writerow(dic.values())
    f.close()
    resp.close()
    print(f"第{page}页写完")
    page += 1
print("over!!")
