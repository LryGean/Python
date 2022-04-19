from lxml import etree

xml = '''
<book>
    <id>1</id>
    <name>云边有个小卖部</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id="10086">周大强</nick>
        <nick id="10010">周芷若</nick>
        <nick class="joy">周杰伦</nick>
        <nick class="jolin">蔡依林</nick>
        <div>
            <nick>孙子节点</nick>
        </div>
        <span>
            <nick>孙子节点</nick>
            <div>
                <nick>重孙子节点</nick>
            </div>
        </span>
    </author>

    <partner>
        <nick id="ppc">冰墩墩</nick>
        <nick id="ppbc">雪容融</nick>
    </partner>
</book>
'''

# etree:XML、HTML、parse（加载一个文件）
tree = etree.XML(xml)
# result = tree.xpath("/book")    # /表示层级关系，，  第一个/表示根节点
# [<Element book at 0x234b3c6dbc8>]

# 取name节点中的文本节点
# result = tree.xpath("/book/name/text()")
# ['云边有个小卖部']

# author下的nick
# result = tree.xpath("/book/author/nick/text()")
# ['周大强', '周芷若', '周杰伦', '蔡依林']

# div下nick节点的文本
# result = tree.xpath("/book/author/div/nick/text()")
# ['惹了']

# author下所有的nick节点（//后代节点）
# result = tree.xpath("/book/author//nick/text()")
# ['周大强', '周芷若', '周杰伦', '蔡依林', '孙子节点', '孙子节点', '重孙子节点']

# 取出author任意子节点包含nick的文本
# result = tree.xpath("/book/author/*/nick/text()")
# ['孙子节点', '孙子节点']

# 匹配book下所有的nick文本
result = tree.xpath("/book//nick/text()")
# ['臭豆腐', '周大强', '周芷若', '周杰伦', '蔡依林', '孙子节点', '孙子节点', '重孙子节点', '冰墩墩', '雪容融']

print(result)
