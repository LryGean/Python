#
# 在____________上补充代码
#

import random

random.seed(25)
n = random.randint(1,100)
for m in range(1,7):
    x = eval(input("请输入猜测数字："))
    if x == n:
        print("恭喜你，猜对了！")
        break
    elif x>n:
        print("大了，再试试")
    else:
        print("小了，再试试")
    if m==6:
        print("谢谢！请休息后再猜")