import re

s = 'life is short,I use python, I love python'

# 取life和python之间的单词
# r = re.search('life(.*)python', s)

# group中的参数表示组号，默认为0
# 完整匹配组号为0
# print(r.group(0))
#结果：life is short,I use python

# print(r.group(1))
#结果： is short,I use 


# 对比findall
# r1 = re.findall('life(.*)python', s)
# print(r1)
# 结果：[' is short,I use ']

r1 = re.search('life(.*)python(.*)python', s)
# print(r1.group(0))
# # 结果：life is short,I use python, I love python

# print(r1.group(1))
# # 结果：is short,I use

# print(r1.group(2))
# # 结果：, I love 


# print(r1.group(0,1,2))
# # 结果：('life is short,I use python, I love python', ' is short,I use ', ', I love ')

print(r1.groups())
# 结果：(' is short,I use ', ', I love ')