# 请在______处使用一行代码或表达式替换
#
# 注意：请不要修改其他已给出代码

import random

s = input("请输入随机种子: ")
ls = []
for i in range(26):
    ls.append(chr(ord('a')+i))
for i in range(10):
    ls.append(chr(ord('0')+i))

random.seed(eval(s))
for i in range(10):
    for j in range(8):
        print(random.choice(ls),end='')
    print()
