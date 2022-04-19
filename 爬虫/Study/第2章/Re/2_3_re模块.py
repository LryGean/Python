import re

num = "我的电话是：10086, 我女朋友的电话是：10010"

# findall：匹配字符串中所有符合正则的内容
# lst = re.findall(r"\d+", num)
# print(lst)
# 结果：['10086', '10010']


# # finditer：匹配字符串中所有的内容【返回的是迭代器，从迭代器中拿到内容需要.group()】
# it = re.finditer(r"\d+", num)
# print(it)
# for i in it:
#     print(i)
#     print(i.group())
# # 结果：
# <callable_iterator object at 0x000002503285E388>
# <re.Match object; span=(6, 11), match='10086'>
# 10086
# <re.Match object; span=(22, 27), match='10010'>
# 10010


# search返回的结果是Match对象，拿到数据需要.group()
# 特点：找到一个结果就返回
# s = re.search(r"\d+", num)
# print(s.group())
# 结果：10086

# match是从头开始匹配的
# m = re.match(r"\d+", num)
# print(m)
# 结果：None

# 预加载(compile)正则表达式
# 实现一个正则多个字符串使用
# obj = re.compile(r"\d+")  # 加快运行速度
# ret = obj.finditer(num)
# # print(ret)
#
# for it in ret:
#     print(it.group())
#
# a = "呵呵哒，我就不信你不还我100000000"
# ret = obj.findall(a)
# print(ret)


s = '''
<div class='jay'><span id='1'>周杰伦</span></div>
<div class='jj'><span id='2'>林俊杰</span></div>
<div class='jolin'><span id='3'>华晨宇</span></div>
<div class='sylay'><span id='4'>汪苏泷</span></div> 
<div class='tory'><span id=5'>林宥嘉</span></div> 
'''

# （?P<分组名字>正则表达式） 可以单独CS正则匹配的内容中进一步提取内容
obj = re.compile(r"<div class='(?P<class>.*?)'><span id='(?P<id>\d+)'>(?P<name>.*?)</span></div>", re.S)  # re.S: 让.能匹配换行符

result = obj.finditer(s)
for it in result:
    print(it.group("class"))
    print(it.group("id"))
    print(it.group("name"))
    print("---------------")


