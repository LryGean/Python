# None

# print(type(None))
# 结果：<class 'NoneType'>   None是一个对象类型


def fun():
    return None

a = fun()

if not a:
    print('S')
else:
    print('F')

if a is None:
    print('S')
else:
    print('F')
# 结果：
# S
# S



a1 = []

# 对a1进行逻辑判断
if not a1:
    print('S')
else:
    print('F')

# if a1    判空操作
if a1 is None:
    print('S')
else:
    print('F')
# 结果：
# S
# F


# None：'不存在'
# False：'假'