# 请在...处使用一行或多行代码替换
#
# 注意：请不要修改其他已给出代码


n = eval(input("请输入数量："))
cost = 160
if n == 1:
    cost = 160
elif n >= 2 and n <= 4:
    cost *= 0.9
    cost = int(cost)
elif n >= 5 and n <= 9:
    cost *= 0.8
    cost = int(cost)
else:
    cost *= 0.7
    cost = int(cost)
print("总额为:",cost)
