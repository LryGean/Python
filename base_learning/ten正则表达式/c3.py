import re 

b = 'C0C++7Java8C#9Python6Javascript'

# 提取字符串中的所有数字

# 方法一：循环遍历
# c = []
# for i in b:
#     if i>='0' and i<='9':
#         c.append(i)
# print(c)

# 'Python'：普通字符
# '\d'：元字符

# 方法二：正则表达式
# 抽象符号：\d,表示0~9
r = re.findall('\d',b)
print(r)


# 匹配非数字
e = re.findall('\D',b)
print(e)