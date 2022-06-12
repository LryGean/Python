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
print(type(soup))
# parent
# title_tag = soup.title
# print(title_tag, title_tag.parent)

# html的对象是soup对象
# print(soup.html.parent, "\n", type(soup.html.parent))

# parents
a_tag = soup.a
# print(a_tag.parents)
for i in a_tag.parents:
    # 直接获取标签名
    print(i.name)
