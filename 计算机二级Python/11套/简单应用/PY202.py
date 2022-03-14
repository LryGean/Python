# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

f = open('data.txt', 'r',encoding="utf-8")
d1 = {}
d2 = {}
unis = {}
for line in f:
    li = [0,""]
    l = line.replace("\n","").split(",")
    if l == ['']:
        continue
    else:
        d1[l[2]] = d1.get(l[2],0) + 1
        d2[l[2]] = d2.get(l[2],"") + " " + l[1]
        li[0] = d1[l[2]]
        li[1] = d2[l[2]]
        unis[l[2]] = li
        
for d in unis:
    print('{:>4}: {:>4} : {}'.format(d,unis[d][0],unis[d][1]))
