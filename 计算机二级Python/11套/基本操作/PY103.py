# 请在______处使用一行代码或表达式替换
#
# 注意：请不要修改其他已给出代码

s = input("请输入一组数据: ")
ls = s.split(',')
lt = []
for i in ls:
    lt.append(eval(i))
print(max(lt))
