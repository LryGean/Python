# 实现装饰器

import time

# 装饰器（打印时间）
def decorctor(func):
    # 添加可变参数, 任意数量的关键字参数（字典形式）
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)
    return wrapper

@decorctor
def f1(func_name):
    print('This is a function named ' + func_name)


f1('test func')
# 结果：
# 1643810737.7933657
# This is a function named test func

print("---------------------------")

#多个参数的函数 
@decorctor
def f2(func_name1, func_name2):
    print('This is a function named ' + func_name1)
    print('This is a function named ' + func_name2)

f2('test func1', 'test func2')
# 结果：
# 1643811584.0773811
# This is a function named test func1
# This is a function named test func2

print("---------------------------")

# 支持关键字参数
@decorctor
def f3(func_name1, func_name2, **kw):
    print('This is a function named ' + func_name1)
    print('This is a function named ' + func_name2)
    print(kw)

f3('test func1', 'test func2', a=1, b=2, c='123')
# 结果：
# 1643812278.006565
# This is a function named test func1
# This is a function named test func2
# {'a': 1, 'b': 2, 'c': '123'}