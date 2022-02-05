# 字符集
import re
s = 'abc, acc, adc, aec, afc, ahc'

# 查找中间字符是c或f的单词
# r = re.findall('a[cfd]c', s)
# print(r)
# ['acc', 'adc', 'afc']

# ^表示不在指定范围
# e = re.findall('a[^cfd]c', s)
# print(e)
# ['abc', 'aec', 'ahc']

# -简化范围
f = re.findall('a[c-f]c', s)
print(f)
# ['acc', 'adc', 'aec', 'afc']