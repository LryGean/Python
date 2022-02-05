# 数量词
 
import re

# 第一个培python少了一个n
# 第二个python正常
# 第三个python多了一个n
a = 'pytho 0 python 1 pythonn 2'


# * ：允许 * 号前的字符匹配0次或者无限多次
# r = re.findall('python*',a)
# 结果：['pytho', 'python', 'pythonn']



# + ：允许 + 号前的字符匹配1次或无限多次
# r = re.findall('python+',a)
# 结果：['python', 'pythonn']



# ? ：允许 ? 号前的字符匹配0次或1次
r = re.findall('python?',a)
# 结果：['pytho', 'python', 'python']

print(r)


# 对比贪婪与非贪婪的 ?
m = re.findall('python{1,2}?',a)
print(m)
# 结果：['python', 'pythonn']
n = re.findall('python{1,2}?',a)
print(n)
# 结果：['python', 'python']