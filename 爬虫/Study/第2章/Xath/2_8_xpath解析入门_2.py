from lxml import etree

tree = etree.parse("b.html")
# result = tree.xpath('/html')

# result = tree.xpath('/html/body/ul/li/a/text()')

# 获取指定的标签内容
# 获取百度文本（xpath的顺序是从1开始数的）
# result = tree.xpath('/html/body/ul/li[1]/a/text()')

# 选取指定标签属性的文本（属性筛选）
# result = tree.xpath("/html/body/ol/li/a[@href='dapao']/text()")

# print(result)

# 遍历ol里的li标签
ol_li_list = tree.xpath('/html/body/ol/li')
for li in ol_li_list:
    # print(li)
    # 在li继续寻找，相对查找
    # ./：表示当前节点
    result1 = li.xpath("./a/text()")
    # print(result1)
    # 获取属性值
    result2 = li.xpath("./a/@href")
    # print(result2)

print(tree.xpath("/html/body/ul/li/a/@href"))
# ['http://www.baidu.com', 'http://www.goole.com', 'http://www.sogou.com']

# 快捷获取xpath：通过检查定位标签位置，复制xpath
print(tree.xpath('/html/body/div[1]/text()'))
