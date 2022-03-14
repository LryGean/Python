#
# 在____________上补充代码
#

import turtle as t
color = ['red','green','blue']
rs = [10,30,60]

for i in range(3):
    t.penup()
    t.goto(0, -rs[i])
    t.pendown() 
    t.pencolor(color[i])
    t.circle(rs[i])
t.done()
