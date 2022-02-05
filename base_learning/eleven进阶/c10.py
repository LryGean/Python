# 旅行者

origin = 0 
def factory(pos):
    
    def go(step):
        # 强制声明pos不是本地局部变量
        nonlocal pos
        new_pos = pos + step   # pos 不声明会被认为是本地局部变量
        pos = new_pos
        return pos
    return go

tourist = factory(origin)
print(tourist(2))
# print(origin)  # 全局变量没有被改变
print(tourist.__closure__[0].cell_contents)   # 记住保存住的pos环境变量

print(tourist(3))
# print(origin)
print(tourist.__closure__[0].cell_contents)

print(tourist(5))
# print(origin)
print(tourist.__closure__[0].cell_contents)


# 非闭包
""" 
origin = 0

def go(step):
    global origin
    new_pos = origin + step
    origin = new_pos
    return origin
print(go(2))
print(go(3))
print(go(5))  
"""



