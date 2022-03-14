# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

data = input()  # 姓名 年龄 性别
# 定义人数
n = 0 
# 定义总年龄
age = 0
# 定义男人数
man_num = 0
while data:
    if data == '\n':
        break
    n += 1
    ls = data.split()
    age += int(ls[2])
    if ls[1] == '男':
        man_num += 1
    data = input()
avg = age/n
print("平均年龄是{:.2f} 男性人数是{}".format(avg,man_num))