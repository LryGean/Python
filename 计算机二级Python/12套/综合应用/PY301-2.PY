# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

import jieba

f = open("八十天环游地球.txt",encoding="utf-8")
txt = f.read()
l = txt.split("□ 作者：儒勒·凡尔纳")
for i in l[:-1]:
    d = {}
    l1 = jieba.lcut(i)
    for j in l1:
        if len(j) >= 2:
            d[j] = d.get(j,0) + 1
    L = list(d.items())
    L.sort(key = lambda x:x[1], reverse=True)
    a = i.split("　")
    print("{0} {1} {2}".format(a[0],L[0][0],L[0][1]))    
f.close()
