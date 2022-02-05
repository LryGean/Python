# re.match
# re.search

import re

s = '83C721D8E67'


# 从字符串首字母开始匹配，如果没有匹配到，返回None
r1 = re.match('\d', s)
print(r1)
print(r1.span())
print(r1.group())
# 结果：<re.Match object; span=(0, 1), match='8'>

# 搜索整个字符串，直到找到第一个符合的正则表达式，然后返回结果
r2 = re.search('\d', s)
print(r2)
# 结果：<re.Match object; span=(1, 2), match='8'>

# match、search对比findall，匹配次数仅为1
r3 = re.findall('\d', s)
print(r3)