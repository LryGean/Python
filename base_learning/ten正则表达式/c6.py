# 数量词
import re
a = 'python 1111java678php'
# 只能匹配一个字符
# r = re.findall('[a-z]',a)
# 结果：['p', 'y', 't', 'h', 'o', 'n', 'j', 'a', 'v', 'a', 'p', 'h', 'p']

# 方法一
# r = re.findall('[a-z][a-z][a-z]',a)
# 结果：['pyt', 'hon', 'jav', 'php']


# 方法二
# 花括号内的参数是需要匹配的个数
# 贪婪
# r = re.findall('[a-z]{3,6}',a)
# 结果：['python', 'java', 'php']

# python默认匹配是会倾向于贪婪的原则，会先以最大的范围匹配，超出范围将非贪婪

# 非贪婪
# 在最后加上问号表示非贪婪
r = re.findall('[a-z]{3,6}?',a)
# 等价于:
# r = re.findall('[a-z]{3}',a)
# 结果：['pyt', 'hon', 'jav', 'php']


print(r)