# 请在______处使用一行代码或表达式替换
#
# 注意：请不要修改其他已给出代码


import time
t = input("请输入一个浮点数时间信息: ")
s = time.ctime(eval(t))
ls = s.split()
print(ls[3][0:2])

