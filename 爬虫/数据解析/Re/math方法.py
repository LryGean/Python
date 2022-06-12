import re

pattern = 'python'

s = 'python and math'
result = re.match(pattern, s)
print(result.group())
