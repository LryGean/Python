import re

# 匹配abc
# pat = re.compile('abc', re.I)
# res = pat.match('Abc123')
# print(res.group())

# 只从第一个找,懒惰原则
# r = re.match('abc', '123abc123abc')
# print(r)

# r = re.search('abc', '123abc123abc')
# print(r.group())

# r = re.findall('abc', '123abc123abc')
# print(r)

# split
# s = '3+4-5*6/7'
# \+
# \-
# \*
# \/
# print(re.split('[\+\-\*\/]', s))

# sub:替换
# s = 'i am Gean, i study python'
# # i-I
# print(re.sub('i', 'I', s))

h = '''ldf
dfsf
dfs
dsf
df
'''

print(re.match('.*', h, re.S).group())
