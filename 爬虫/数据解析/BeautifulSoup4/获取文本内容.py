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
title_tag = soup.title

# print(title_tag.string)    # 获取标签里面的文本内容

# 通过爷爷标签获取内容
# head_tag = soup.head
# print(head_tag.string)

# 如果标签tag包含多个子节点，tag无法确定内容，返回None
# texts = soup.html.string
# print(texts)

# texts = soup.html.strings
# 去除多个换行符
texts = soup.html.stripped_strings
# print(texts)
for i in texts:
    print(i)


