'''
def funcname(parameter_list)
    pass
'''

# 1.参数列表可以没有
# 2.return value  (若无return，则默认返回None)

# import sys
# #设置最大递归层数
# sys.setrecursionlimit(1000000)

def add(x,y):
    result = x + y
    return result
a = add(1,2)

def print_code(code):
    print(code)
b = print_code("Python")
print(a,b)