# 类：map

# 适用场景

# 列表中的每一个数进行平方，再组成新的列表
from numpy import square


list_x = [1,2,3,4,5,6,7,8]

# 方法一
# 循环实现（常规方案）
# a = []
# for x in list_x:
#     a.append(square(x))
# print(a)
# 结果：[1, 4, 9, 16, 25, 36, 49, 64]

# 方法二
def square(x):
    return x * x

# map会对所传入的集合的每一项传入函数中，并接收结果
# 作用：一一映射
r1 = map(square, list_x)

# print(map)
# # 结果:<class 'map'>

# print(r1)
# # 结果:<map object at 0x000001B6D8B6BFA0>

# print(list(r1))
# # 结果:[1, 4, 9, 16, 25, 36, 49, 64]

# 方法三
# 用lambda表达式等价替换r1 
r2 = map(lambda x : x*x, list_x)
print(list(r2))
# 结果：[1, 4, 9, 16, 25, 36, 49, 64]

# 传入多个列表
list_y = [1,2,3,4,5,6,7,8]    # 新增参数列表y
r3 =  map(lambda x, y : x*x + y, list_x,list_y)     # map计算的个数是参数列表中长度较小的
print(list(r3))
# 结果：[2, 6, 12, 20, 30, 42, 56, 72]
