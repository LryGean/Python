from bs4 import BeautifulSoup

html_doc = """<a>
<b>bbb</b><c>ccc</c><d>ddd</d>
</a>
"""

# 创建对象
soup = BeautifulSoup(html_doc, 'lxml')

b_tag = soup.b
# print(b_tag)
# print(b_tag.next_sibling)   # 下一个兄弟节点： c
# print(b_tag.next_siblings)
# for i in b_tag.next_siblings:
#     print(i)




