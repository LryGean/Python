# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

f = open("八十天环游地球.txt", encoding="utf-8")
f1 = open("八十天环游地球-章节.txt", "w")
txt = f.readlines()
for i in txt:
    if "　" in i:
        f1.write(i)
f1.close()
f.close()

