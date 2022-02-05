#### 函数式编程 ###

# 闭包 = 函数 + 环境变量  (环境定义时候)
# 现场

def curve_pre1():
    # 环境变量
    a = 25

    # 抛物线
    def curve(x):
        return a*x*x
    return curve

# f = curve_pre()
# print(f(2))

a = 10
f = curve_pre1()
# curve(2)
print(f(2))

# 闭包被保存
print(f.__closure__)
# 结果：(<cell at 0x000002B6F291BFD0: int object at 0x000002B6F2036C30>,)

# 取出闭包的环境变量
print(f.__closure__[0].cell_contents)
# 结果：25



def curve_pre2():
    # 环境变量
    a = 30

    # 抛物线
    def curve(x):
        return a*x*x
    return curve

