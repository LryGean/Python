import turtle
from random import randrange

# 定义一条蛇
snake = [[0,0],[0,10],[0,20]]

food = [-10,0]


def square(x, y, size, color):
    # 抬起画笔
    turtle.penup()   
    turtle.goto(x, y)
    # 放下画笔
    turtle.pendown()
    # 设置贪吃蛇的颜色
    turtle.color(color)
    # 渲染
    turtle.begin_fill()
    # 画正方形（循环四次）
    for i in range(4):
        turtle.forward(size)  # 每一次画一定的长度
        turtle.left(90)       # 每一次转90°
    turtle.end_fill()

# 判断边界条件（碰条件）
def inside(head):
    return -250<head[0]<250 and -250<head[1]<250

def change_direction(x, y):
    aim[0] = x
    aim[1] = y

# 蛇移动
# 移动逻辑：头部添加一个方块，移动方向取决于蛇头部添加的位置，尾部消除一个方块
import copy
# 移动的方向
aim = [0, 10]
def snake_move():
    # 用蛇的最后一个身体作为头部
    # 需要将头部拷贝（深度拷贝）
    head = copy.deepcopy(snake[-1])
    head = [head[0] + aim[0], head[1]+aim[1]]
    print(head)
    # 判断游戏退出条件（头吃到尾巴或者头不在边界内）
    if head in snake or not inside(head):
        print("game over")
        square(head[0],head[1],10,'red')
        return
    # 判断是否吃到实物（头部和食物坐标重合时）
    if head == food:
        food[0] = randrange(-15,15)*10
        food[1] = randrange(-15,15)*10
    else:
        snake.pop(0)
    snake.append(head)    # 头部添加一个方块
    # snake.pop(0)          # 尾巴去除一个方块
    turtle.clear()        # 删除之前的动画
    # 画出食物
    square(food[0], food[1], 10, 'green')
    for body in snake:
        square(body[0], body[1], 10, 'black')
    # 循环移动函数，每300ms执行一次
    turtle.update()
    turtle.ontimer(snake_move, 200)


turtle.setup(500,500)  # 定死屏幕宽度
turtle.tracer(False)
turtle.hideturtle()    # 去掉箭头
turtle.listen()        # 监听键盘
# 上移
turtle.onkey(lambda: change_direction(0, 10), 'Up')
# 下移
turtle.onkey(lambda: change_direction(0, -10), 'Down')   
# 左移
turtle.onkey(lambda: change_direction(-10, 0), 'Left')
# 右移
turtle.onkey(lambda: change_direction(10, 0), 'Right')
snake_move()
turtle.done()          # 不让屏幕立马关闭