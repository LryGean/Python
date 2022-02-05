
students = {
        '小明' : 18,
        '小亮' : 19,
        '小红' : 17,
        '小宇' : 20,
}

# 提取key
s = [key for key,value in students.items()]
print(s)

# 颠倒key和value
b = {value:key for key,value in students.items()}
print(b)

# 元组形式(不可变序列)
c = (key for key,value in students.items())
print(c)
# 结果：<generator object <genexpr> at 0x000001ACE6039D60>      可变对象
for x in c:
    print(x)