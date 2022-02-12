import turtle as a

a.screensize(400,300)#设置屏幕大小

a.setup(width=400,height=300)#设置画布大小

a.pensize(15)

a.speed(15)#设置画笔速度

a.hideturtle()#隐藏画笔

a.penup()#提笔

a.goto(-100,100)#移动画笔位置

a.setheading(180)#设置朝向正西

a.pencolor("pink")

a.pendown()#放笔

a.circle(200)

a.penup()#取名

a.goto(-150,10)

yourname=a.textinput("请老实回答","你的名字是？")

name=yourname+"崽崽"

a.pendown()

a.write(name,font=("elephant",25,"bold"))#打印文本
#画眼睛
a.penup()#画左眼

a.goto(-200,0)

a.pendown()

a.circle(25)

a.penup()

a.goto(-200,-14)

a.pendown()

a.circle(9)

a.penup()#光晕

a.goto(-190,-20)

a.pencolor("white")

a.pendown()

a.dot(10)

a.penup()#画右眼

a.pencolor("pink")

a.goto(0,0)

a.pendown()

a.circle(25)

a.penup()#光晕

a.goto(0,-14)

a.pendown()

a.circle(9)

a.penup()

a.goto(-10,-20)

a.pencolor("white")

a.pendown()

a.dot(10)
#画鼻子
a.penup()#画鼻子

a.speed(30)#设置画笔速度

a.pencolor("pink")

a.goto(-150,-75)

a.setheading(45)

a.pendown()

for i in range(90):

    a.forward(1.5)

    a.right(1)

for i in range(3): #圆化棱角，每转16度向前走3个像素

    a.right(16)

    a.forward(3)

    a.forward(15)

for i in range(3): #圆化棱角

    a.right(16)

    a.forward(3)

    a.setheading(225)

for i in range(90):

    a.forward(1.5)

    a.right(1)

for i in range(3): #圆化棱角

    a.right(16)

    a.forward(3)

    a.forward(15)

for i in range(3): #圆化棱角

    a.right(16)

    a.forward(3)

a.penup()

a.speed(5)#设置画笔速度

a.goto(-125,-70)#第一条杠

a.setheading(270)

a.pendown()

a.forward(50)

a.penup()

a.goto(-70,-65)#第二条杠

a.pendown()

a.forward(55)

a.penup()#画嘴巴

a.speed(30)#设置画笔速度

a.goto(-135,-165)

a.setheading(305)

a.pendown()

for i in range(120):

    a.forward(1)

    a.left(1)

a.penup()#画右耳朵

a.speed(5)

a.setheading(0)

a.goto(-17,90)

a.pendown()

a.forward(60)

a.penup()

a.goto(28,75)#跳到下一笔起始位置

a.setheading(45)

a.pendown()

a.forward(110)

a.right(45)

a.forward(40)

a.setheading(225)

a.forward(40)

a.setheading(270)

for i in range(7): #圆化棱角

    a.right(2.5)

    a.forward(10)

    a.forward(80)

a.penup()#画左耳朵

a.goto(-183,90)

a.setheading(180)

a.pendown()

a.forward(60)

a.penup()

a.goto(-230,75)#跳到下一笔起始位置

a.setheading(135)

a.pendown()

a.forward(110)

a.left(45)

a.forward(40)

a.setheading(-45)

a.forward(40)

a.setheading(270)

for i in range(10): #圆化棱角

    a.left(2.5)

    a.forward(15)

a.penup()#画左腮红

a.pencolor("tomato")#设置成番茄色

a.goto(-250,-100)

a.setheading(270)

a.pendown()

a.forward(20)

a.penup()

a.goto(-210,-100)

a.pendown()

a.forward(20)

a.penup()#画右腮红

a.goto(10,-100)

a.pendown()

a.forward(20)

a.penup()

a.goto(50,-100)

a.pendown()

a.forward(20)

a.done() #留存图像在画布上



