# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准


f = open("sensor.txt", "r", encoding="utf-8")
fo = open("earpa001.txt", "w", encoding="utf-8")
txt = f.readlines()
for line in txt:
    s = line.split(",")
    l = []
    if s[1] == " earpa001":
        l = line.split(",")
        print(l[0],l[1],l[2],l[3][:-1])
        fo.write('{},{},{},{}\n'.format(l[0],l[1],l[2],l[3][:-1]))
fo.close()
f.close()