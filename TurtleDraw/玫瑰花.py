import turtle


turtle.setup(940,850)
turtle.speed(10)#画笔移动的速度
#turtle.bgcolor('orange')
#turtle.bgcolor()
turtle.bgpic()
turtle.bgpic(r'C:\Users\ASUS\Desktop\VSCode V1.30.1 汉化版\画画\背景2.gif')

"""
①字体风格：
normal：文本正常显示
italic：文本斜体显示
oblique：文本倾斜显示
②字体风格：
normal：显示标准字体
small-caps：显示小型大写字母的字体
③字体加粗：
normal：标准的字符
bold：粗体字符
bolder：更粗的字符
lighter：更细的字符
"""

turtle.color("#FF77FF")
turtle.setposition(-45,235)
turtle.write("~七夕快乐~",font=("华文彩云",25,'bold'))

#设置初始位置
turtle.penup()
turtle.goto(-50,0)
turtle.pencolor("#444444")
turtle.left(90)  #逆时针转动画笔90°
turtle.fd(200)
turtle.pendown()
turtle.right(90)
#设置画笔大小
turtle.pensize(2)
#花蕊
turtle.fillcolor("#B94FFF")
turtle.begin_fill()
turtle.circle(10,180)
turtle.circle(25,110)
turtle.left(50)
turtle.circle(60,45)
turtle.circle(20,170)
turtle.right(24)
turtle.fd(30)
turtle.left(10)
turtle.circle(30,110)
turtle.fd(20)
turtle.left(40)
turtle.circle(90,70)
turtle.circle(30,150)
turtle.right(30)
turtle.fd(15)
turtle.circle(80,90)
turtle.left(15)
turtle.fd(45)
turtle.right(165)
turtle.fd(20)
turtle.left(155)
turtle.circle(150,80)
turtle.left(50)
turtle.circle(150,90)
turtle.end_fill()

#花瓣1
turtle.left(150)
turtle.circle(-90,70)
turtle.left(20)
turtle.circle(75,105)
turtle.setheading(60)
turtle.circle(80,98)
turtle.circle(-90,40)

#花瓣2
turtle.left(180)
turtle.circle(90,40)
turtle.circle(-80,98)
turtle.setheading(-83)

#叶子1
turtle.fd(30)
turtle.left(90)
turtle.fd(25)
turtle.left(45)
turtle.fillcolor("#66FF66")
turtle.begin_fill()
turtle.circle(-80,90)
turtle.right(90)
turtle.circle(-80,90)
turtle.end_fill()

turtle.left(135+90)
turtle.fd(60)
turtle.left(180)
turtle.fd(85)
turtle.left(90)
turtle.fd(80)

#叶子2
turtle.right(90)
turtle.right(45)
turtle.fillcolor("#66FF66")
turtle.begin_fill()
turtle.circle(80,90)
turtle.left(90)
turtle.circle(80,90)
turtle.end_fill()

turtle.left(135)
turtle.fd(60)
turtle.left(180)
turtle.fd(60)
turtle.right(90)
turtle.circle(200,60)
turtle.pencolor("#B94FFF")
turtle.write("哈哈哈哈，\n快来看呐！\n送你个玫瑰花，\n希望你能开心！\nღ( ´･ᴗ･` )比心",font=("华文彩云",16,'normal','bold'))
turtle.done()
