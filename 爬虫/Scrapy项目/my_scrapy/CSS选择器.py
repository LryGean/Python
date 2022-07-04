# from bs4 import BeautifulSoup
import parsel

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
# soup = BeautifulSoup(html_doc, 'lxml')

# 通过属性查找
# print(soup.select('a["http://example.com/tillie"]'))

# print(soup.select('a#link1')[0]['href'])
# # 建议使用，提取不到，返回为空
# print(soup.select('a#link1')[0].get('href'))


select = parsel.Selector(html_doc)
# re
# print(select.re('\\d+'))

# xpath
# print(select.xpath('//p[@class="story"]').get())
# print(select.xpath('//p[@class="story"]').getall())


# css
# 1.通过标签名查找
# 获取一个
# print(select.css('a').get())
# print(select.css('a').getall())

# 2.通过类名查找
# print(select.css('.sister').get())

# 3.通过id查找
# print(select.css('#link1'))
# print(select.css('#link1').get())

# 获取内容
# print(select.css('#link1::attr(href)').get())
print(select.css('#link1::text').get())


