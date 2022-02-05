# 实现装饰器

import time

# 装饰器
def decorctor(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper

@decorctor
def f1():
    print('This is a function')


# 方法一： 
# f = decorctor(f1)
# f()
# 结果：
# 1643732786.3145547
# This is a function


# 方法二：
f1()
# 结果：
# 1643732786.3145547
# This is a function