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

# 找所有的a标签
# print(soup.select('a'))

# 通过class='sister' 找标签
# print(soup.select('.sister'))

# 通过id值
# print(soup.select('#link1'))

# 获取title标签中的文本内容
print(soup.select('title')[0].string)   # 找全部，把结果放在列表中
# 扩展方法: get_text
print(soup.select('title')[0].get_text())
