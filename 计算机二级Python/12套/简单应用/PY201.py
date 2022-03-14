# 请在______处使用一行代码或表达式替换
#
# 注意：请不要修改其他已给出代码

import turtle as t
import random as r
r.seed(1)
t.pensize(2)
for i in range(3):
    length = r.randint(20,80)
    x0 = r.randint(-100, 100)
    y0 = r.randint(-100, 100)

    t.penup()
    t.goto(x0,y0)
    t.pendown()
    for j in range(4):
        t.fd(length)
        t.seth(90*(j+1))
t.done()
