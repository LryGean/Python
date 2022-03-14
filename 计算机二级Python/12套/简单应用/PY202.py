# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

sumtime = 0
percls = []
ts = {}
with open('out.txt', 'r') as f:
    txt = f.readlines()
    n = 0
    for i in txt:
        percls= i.split(",")
        sumtime += eval(percls[1])
        # 0表示默认值
        ts[percls[0]] = ts.get(percls[0],0) + eval(percls[2][:-1])

print('the total execute time is ', sumtime)
tns = list(ts.items())
tns.sort(key=lambda x: x[1], reverse=True)
for i in range(3):
    print('the top {} percentage time is {}, spent in "{}" operation'.format(i, tns[i][1],tns[i][0]))