import re

# .
# result = re.match('a.cde', 'abcde')
#
# print(result)

# |
# print(re.match('a|b', 'a'))
# print(re.match('a|b', 'b'))
# print(re.match('a|b', 'ab'))
# print(re.match('a|b', 'bc'))
# print(re.match('a|b', 'ca'))  # 惰性原则

# []——匹配字符集中的一个字符
# print(re.match('[123abc]', '3a'))
# print(re.match('[123abc]a', '3a'))

s = r'使用\n,能够换行'
# s2 = re.match('使用\\\\n,能够换行', s)
s2 = re.match(r'使用\\n,能够换行', s)
print(s2.group())
