# 闭包函数  （只是函数式编程的一种应用）

def f1():
    a = 10       # 环境变量
    
    def f2():
        # 局部变量
        # a = 20
        # print(a)

        # 引用环境变量 ：被视为是闭包
        return a
    return f2

    # print(a)
    # 10
    
    # f2()
    # 20

    # print(a)
    # 10

f = f1()

# 验证闭包
print(f)
# 结果：<function f1.<locals>.f2 at 0x0000024A1C3ECA60>
print(f.__closure__)
# 结果：None
# (<cell at 0x0000020D02B89700: int object at 0x0000020D02486A50>,)