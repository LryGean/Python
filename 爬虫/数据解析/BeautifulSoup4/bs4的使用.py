from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# 创建对象
soup = BeautifulSoup(html_doc, 'lxml')
# 格式化处理网页原码
print(soup.prettify())
# 获取文本内容
# print(soup.title.string)
# 找一个
# print(soup.find('p'))
# 找全部
# print(soup.find_all('p'))

# 需求：找a标签的href的属性
links = soup.find_all('a')
for link in links:
    print(link.get('href'))
