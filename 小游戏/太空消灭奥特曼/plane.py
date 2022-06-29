import pygame
import random
import math

# 1.初始化界面
pygame.init()
# 设置窗口
screen = pygame.display.set_mode((1280, 720))
# 设置标题
pygame.display.set_caption("太空消灭奥特曼")
icon = pygame.image.load('./img/UFO.webp')
pygame.display.set_icon(icon)
bgImg = pygame.image.load('./img/bg.webp')

# 音效
# 背景音效
a = pygame.mixer.music.load('./music/晴天.mp3')
pygame.mixer.music.play(-1)
# pygame.mixer.music.set_volume(5)
# 创建击中音效
bao_sound = pygame.mixer.Sound('./music/爆炸.wav')
bao_sound.set_volume(0.1)

# 5.飞机
planeImg = pygame.image.load('./img/plane.png')
playerX = 640
playerY = 620
# 玩家移动的速度
playerXStep = 0
playerYStep = 0

# 添加分数
score = 0
# 创字体
# font = pygame.font.Font('freesansbold.ttf', 32)
font = pygame.font.Font('./font/SentyTEA字体_爱给网_aigei_com.ttf', 32)


# 宋体
# font = pygame.font.SysFont('simsunnsimsun', 32)   
# 黑体
# font = pygame.font.SysFont('SimHei', 32)

def show_score():
    text = f'分数：{score}'
    score_render = font.render(text, True, (0, 255, 0))
    screen.blit(score_render, (10, 10))


# 游戏结束
is_over = False


# over = pygame.font.Font('./font/SentyTEA字体_爱给网_aigei_com.ttf', 100)
def check_is_over():
    over = pygame.font.Font('./font/SentyTEA字体_爱给网_aigei_com.ttf', 100)
    end = '游戏结束'
    end_render = over.render(end, True, (0, 255, 0))
    screen.blit(end_render, (640, 360))

sad = pygame.image.load('./img/表情.webp')

# 9.添加敌人
number_of_enemies = 50


# 敌人类
class Enemy():
    def __init__(self):
        self.list = ['凹凸曼', '奥特曼', '迪迦', '雷欧', '泰罗']
        self.name = random.choice(self.list)
        # self.a = random.randint(1,5)
        self.img = pygame.image.load('./img/{}.png'.format(self.name))
        self.x = random.randint(100, 1180)
        self.y = random.randint(50, 250)
        self.step = random.randint(2, 7) / 10  # 敌人移动的速度

    # 重置被击中的敌人
    def reset(self):
        # self.x = random.randint(100,1180)
        # self.y = random.randint(50, 200)
        enemies.remove(self)


enemies = []

for i in range(number_of_enemies):
    enemies.append(Enemy())


def distance(bx, by, ex, ey):
    a = bx - ex
    b = by - ey
    return math.sqrt(a ** 2 + b ** 2)


# print(distance(1,1, 5,4))

# 子弹类
class Bullet():
    def __init__(self):
        self.img = pygame.image.load('./img/子弹.png')
        self.lx = playerX + 25
        self.ly = playerY + 10
        self.rx = playerX + 55
        self.ry = playerY + 10
        self.step = 1

    def hit(self):
        global score
        for e in enemies:
            if distance(self.lx, self.ly, e.x + 30, e.y + 90) < 10 or distance(self.lx, self.ly, e.x + 30,
                                                                               e.y + 90) < 10:
                # 射中
                # 添加击中提示音
                bao_sound.play()
                bullets.remove(self)
                e.reset()
                score += 2
                print(score)


# 保存现有的子弹
bullets = []


# 显示子弹移动
def show_bullets():
    for b in bullets:
        screen.blit(b.img, (b.lx, b.ly))
        screen.blit(b.img, (b.rx, b.ry))
        # 
        b.hit()
        # 移动子弹
        b.ly -= b.step
        b.ry -= b.step
        if b.ly < 0 and b.ry < 0:
            bullets.remove(b)
            break


def show_enemy():
    global is_over
    for e in enemies:
        screen.blit(e.img, (e.x, e.y))
        e.x += e.step
        if e.x > 1180 or e.x < 0:
            e.step *= -1
            e.y += 60
            if e.y > 560:
                is_over = True
                print("游戏结束")
                enemies.clear()
    if enemies == []:
        check_is_over()


def process_events():
    global running, playerXStep, playerYStep
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 通过键盘事件控制飞机的移动
        if event.type == pygame.KEYDOWN:  # 按下就移动
            if event.key == pygame.K_RIGHT:
                playerXStep = 0.5
            elif event.key == pygame.K_LEFT:
                playerXStep = -0.5
            elif event.key == pygame.K_UP:
                playerYStep = 0.5
            elif event.key == pygame.K_DOWN:
                playerYStep = -0.5
            elif event.key == pygame.K_SPACE:
                print('发射子弹')
                # 创建子弹
                bullets.append(Bullet())

        if event.type == pygame.KEYUP:  # 抬起来就不动
            playerXStep = 0
            playerYStep = 0


def move_player():
    global playerX, playerY
    playerX += playerXStep
    playerY -= playerYStep

    # 防止飞机出界
    if playerX > 1210:
        playerX = 1210
    if playerX < -30:
        playerX = -30
    if playerY < 0:
        playerY = 0
    if playerY > 620:
        playerY = 620

# 游戏主循环
running = True
while running:
    # 将背景画在（0,0）坐标上
    screen.blit(bgImg, (0, 0))
    show_score()  # 显示分数

    # 处理键盘事件
    process_events()

    screen.blit(planeImg, (playerX, playerY))

    # 移动玩家
    move_player()

    # 显示敌人
    show_enemy()

    # 显示子弹
    show_bullets()

    if enemies == []:
        check_is_over()
        screen.blit(sad, (150, 250))

    # 画完以后一定要更新
    pygame.display.update()
