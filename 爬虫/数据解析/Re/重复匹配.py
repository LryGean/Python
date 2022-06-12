import re

# {n},表达式
# print(re.match('\d{3}', '1234'))

# {m，n}
# print(re.match('\d{3,4}', '12345'))

# print(re.match('\d{3,}', '123456789'))

# *:0次或多次
# print(re.match('w[a-z]*', 'wasf'))
# print(re.match('w[a-z]*', 'w'))

# +:至少出现一次
# print(re.match('w[a-z]+', 'wasdde'))

# ?:0次或1次
# print(re.match('w[a-z]?', 'wasdde'))

print(re.match('\d{2,3}?', '12343abc'))
