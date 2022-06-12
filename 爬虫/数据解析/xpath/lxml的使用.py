#
from lxml import etree
import csv

wb_data = """
<div>
    <ul>
        <li class="item-0"><a href="link1.html">first item</a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive"><a href="link3.html">third item</a></li>
        <li class="item-1"><a href="link4.html">four item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
</div>
"""

# 1.
html_element = etree.HTML(wb_data)
# print(html_element)

# 2.
links = html_element.xpath('//li/a/@href')
# print(links)
results = html_element.xpath('//li/a/text()')
# print(results)

# 3.
# lis = html_element.xpath('//li')   # []
# for i in lis:
#     a = i.xpath('.//a')
#     print(a)

lst = []
for i in range(len(links)):
    dic = {}
    dic['href'] = links[i]
    dic['title'] = results[i]
    # print(dic)
    lst.append(dic)
print(lst)
