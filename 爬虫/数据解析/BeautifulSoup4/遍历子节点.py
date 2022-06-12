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
head_tag = soup.head

# contents:获取head的子节点， 返回列表数据类型
# print(head_tag.contents)

# children:返回子节点的迭代器
# print(head_tag.children)
# for i in head_tag.children:
#     print(i)

# 返回某个标签的子子孙孙
# print(head_tag.descendants)   # 生成器：循环取
# for i in head_tag.descendants:
#     print(i)

# 获取文本内容

