import re

# print(re.match('1[2345678901]\d{10}$', '123456789019'))

# 贪婪匹配
s = '<div>abc</div><div>bcd</div>'
ptn = '<div>.*?</div>'
# ptn = '</div><div>.*?</div>'
r = re.match(ptn, s)   # 默认贪婪匹配
print(r.group())
# <div>abc</div><div>bcd</div>
