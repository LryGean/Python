# 装饰器

import time

def f1():
    print('This is a function')

f1()
# 结果：1643561961.9926693  时间戳

# 开闭原则：对修改是封闭，对扩展是开放

def f2():
    print('This is a function')


# 未解决多个函数同时需要执行打印当前时间
def print_current_time(func):
    print(time.time())
    func()

print_current_time(f1)
print_current_time(f2)