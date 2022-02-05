#  类：filter（过滤）


# 需求：过滤所有的 0
list_x = [1, 0, 1, 0, 0, 1]

r1 = filter(lambda x: True if x==1 else False, list_x)

print(r1)
# 结果：<filter object at 0x000001E5B3F696D0>

print(list(r1))
# 结果：[1, 1, 1]

# 
# 直接返回x,1是True,0是False会被直接过滤
r2 = filter(lambda x: x, list_x)
print(list(r2))
# 结果：[1, 1, 1]



# 过滤掉小写字母 
list_u = ['a', 'B', 'c', 'F', 'e']
r3 = filter(lambda u: u if u>'A' and u<'Z' else False, list_u)
print(list(r3))

