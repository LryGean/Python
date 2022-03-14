# 请在______处使用一行代码或表达式替换
#
# 注意：请不要修改其他已给出代码

s = input("请输入一个小数: ")
s = s[::-1]
cs = 0
for c in s:
    if c == '.':
        break
    cs += eval(c)
print('{:*>8}'.format(cs))
print('{0:*>8}'.format(cs))
