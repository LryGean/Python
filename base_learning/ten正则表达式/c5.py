#概括字符集
import re
a = 'python 1111 java & 678___php \n \r 嗨 \t'

# \d : 字符集等价方式 
# r = re.findall('[0-9]', a)
# print(r)

# \D : 字符集等价方式
# e = re.findall('[^0-9]', a)
# print(e)



# 单词字符
# \w : 匹配包括下划线的任何单词字符。等价于“[A-Za-z0-9_]”,数字和字母
# f = re.findall('\w', a)
# print(f)

# \W : 非单词字符(包括空格,\n,\r)
# g = re.findall('\W', a)
# print(g)



# 空白字符
# \s : （' ','\n','\r','\t'）
# b = re.findall('\s', a)
# print(b)

# 非空白字符
# \S ：
# c = re.findall('\S', a)
# print(c)

# . ：匹配出换行符\n之外其他所有字符
d = re.findall('.', a)
print(d)