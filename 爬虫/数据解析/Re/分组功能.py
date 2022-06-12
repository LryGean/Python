import re
s = 'banana price is $33, apple price is $55'
# $33 $55
result = re.search('.*(\$\d+).*(\$\d+)', s)
print(result.group())
print(result.group(1))
print(result.group(2))
print(result.group(1, 2))

