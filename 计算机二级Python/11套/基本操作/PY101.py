# 请在______处使用一行代码或表达式替换
#
# 注意：请不要修改其他已给出代码

s = input("请输入一个正整数: ")
cs = 0
for c in s:
    cs += eval(c)
print('{0:=^25}'.format(cs))
