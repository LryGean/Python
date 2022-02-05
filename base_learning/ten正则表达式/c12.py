# 用函数作为参数传递
import re

s = 'A8C3721D86'

# 要求：
# 1.找出所有数字
# 2.大于等于6的替换为9
# 3.小于6的替换为0

def convert(value):
    matched = value.group()
    if int(matched)>=6:
        return '9'
    else:
        return '0'

r = re.sub('\d', convert, s)

print(r)