"""
新增功能：
    完善我方坦克发射子弹

"""
#导入pygame模块
import pygame,time,random

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BG_COLOR = pygame.Color(0,0,0)
TEXT_COLOR=pygame.Color(255,0,0)

class MainGame():
    window=None
    my_tank=None
    #存储敌方坦克的列表
    enemyTankList=[]
    #定义已经生成的敌方坦克的数量
    enemyTankCount=5
    #存储我方子弹的列表
    myBulletList=[]
    def __init__(self):
        pass
    #开始游戏
    def startGame(self):
        #加载主窗口
        #初始化窗口
        pygame.display.init()
        #设置窗口的大小及显示
        MainGame.window=pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
        #初始化我方坦克
        MainGame.my_tank=Tank(350,250)
        #初始化敌方坦克，并将敌方坦克添加到列表中
        self.createEnemyTank()
        #设置窗口的标题
        pygame.display.set_caption("坦克大战1.03")
        while True:
            #使坦克移动的速度慢一点
            time.sleep(0.02)
            #给窗口设置设置填充色
            MainGame.window.fill(BG_COLOR)
            #获取事件
            self.getEvent()
            #绘制文字
            MainGame.window.blit(self.getTextSurface('敌方坦克剩余数量{0}'.format(len(MainGame.enemyTankList))),(10,10))
            #调用坦克显示的方法
            MainGame.my_tank.displayTank()
            #循环遍历敌方坦克列表，展示敌方坦克
            self.blitEnemyTank()
            #循环遍历显示我方坦克的子弹
            self.blitMyBullet()
            #调用移动方法
            #如果坦克的方向开关开启，才可以移动
            if not MainGame.my_tank.stop:
                MainGame.my_tank.move()
            pygame.display.update()

    # 初始化敌方坦克，并将敌方坦克添加到列表中
    def createEnemyTank(self):
        top=100
        #循环生成敌方坦克
        for i in range(MainGame.enemyTankCount):
            left=random.randint(0,600)
            speed=random.randint(1,4)
            enemy=EnemyTank(left,top,speed)
            MainGame.enemyTankList.append(enemy)

    # 循环遍历敌方坦克列表，展示敌方坦克
    def blitEnemyTank(self):
        for enemyTank in MainGame.enemyTankList:
            enemyTank.displayTank()
            enemyTank.randMove()
    #循环遍历我方子弹存储的列表
    def blitMyBullet(self):
        for myBullet in MainGame.myBulletList:
            myBullet.displayBullet()



    #结束游戏
    def endGame(self):
        print("欢迎使用，欢迎下次再用")
        exit()

    #左上角文字的绘制
    def getTextSurface(self,text):
        #初始化字体
        pygame.font.init()
        #查看所有字体名称
        #print(pygame.font.get_fonts())
        #获取字体Font的对象
        font=pygame.font.SysFont('kaiti',18)
        #绘制文字信息
        textSurface=font.render(text,True,TEXT_COLOR)
        return textSurface
    #获取事件
    def getEvent(self):
        #获取所有事件
        eventList=pygame.event.get()
        #遍历事件
        for event in eventList:
            #判断按下的键是关闭还是键盘按下
            #如果按下的是退出，关闭窗口
            if event.type == pygame.QUIT:
                self.endGame()
            #如果是键盘的按下
            if event.type == pygame.KEYDOWN:
                #判断按下的上下左右
                if event.key == pygame.K_LEFT:
                    #切换方向
                    MainGame.my_tank.direction='L'
                    #修改坦克的开关状态
                    MainGame.my_tank.stop=False
                    #MainGame.my_tank.move()
                    print("按下左键，坦克向左移")
                elif event.key == pygame.K_RIGHT:
                    MainGame.my_tank.direction = 'R'
                    # 修改坦克的开关状态
                    MainGame.my_tank.stop = False
                    #MainGame.my_tank.move()
                    print("按下右键，坦克向右移")
                elif event.key == pygame.K_UP:
                    MainGame.my_tank.direction = 'U'
                    # 修改坦克的开关状态
                    MainGame.my_tank.stop = False
                    #MainGame.my_tank.move()
                    print("按下上键，坦克向上移")
                elif event.key == pygame.K_DOWN:
                    MainGame.my_tank.direction = 'D'
                    # 修改坦克的开关状态
                    MainGame.my_tank.stop = False
                    #MainGame.my_tank.move()
                    print("按下下键，坦克向下移")
                elif event.key == pygame.K_SPACE:
                    print("发射子弹")
                    #创建我方子弹
                    myBullet=Bullet(MainGame.my_tank)
                    MainGame.myBulletList.append(myBullet)

            #松开方向键，坦克停止，修改开关
            if event.type == pygame.KEYUP:
                #判断松开的键是上下左右的时候，坦克才停止移动
                if event.key==pygame.K_UP or event.key==pygame.K_DOWN or event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    MainGame.my_tank.stop=True




class Tank():
    #添加距离左边left,距离上边top

    def __init__(self,left,top):
        #保存加载的图片
        self.images = {
            'U':pygame.image.load('image/p1tankU.gif'),
            'D': pygame.image.load('image/p1tankD.gif'),
            'L': pygame.image.load('image/p1tankL.gif'),
            'R': pygame.image.load('image/p1tankR.gif'),
        }
        #方向
        self.direction='U'
        #根据当前图片的方向获取图片
        self.image=self.images[self.direction]
        #获取区域
        self.rect=self.image.get_rect()
        #设置区域的left,top
        self.rect.left=left
        self.rect.top=top
        #速度 决定移动的快慢
        self.speed=10
        #坦克移动的开关
        self.stop=True


    #移动
    def move(self):
        #判断坦克的方向
        if self.direction == 'L':
            if self.rect.left>0:
                self.rect.left -= self.speed
        elif self.direction == 'U':
            if self.rect.top>0:
                self.rect.top -= self.speed
        elif self.direction == 'D':
            if self.rect.top+self.rect.height<SCREEN_HEIGHT:
                self.rect.top += self.speed
        elif self.direction == 'R':
            if self.rect.left+self.rect.height<SCREEN_WIDTH:
                self.rect.left += self.speed
    #射击
    def shot(self):
        pass

    #展示坦克的方法
    def displayTank(self):
        #获取展示的对象
        self.image=self.images[self.direction]
        #调用blit方法展示
        MainGame.window.blit(self.image,self.rect)


#我方坦克
class MyTank(Tank):
    def __init__(self):
        pass

#敌方坦克
class EnemyTank(Tank):
    def __init__(self,left,top,speed):
        #加载图片集
        self.images={
            'U': pygame.image.load('image/enemy1U.png'),
            'D': pygame.image.load('image/enemy1D.png'),
            'L': pygame.image.load('image/enemy1L.png'),
            'R': pygame.image.load('image/enemy1R.png')
        }
        #方向,随机生成敌方坦克方向
        self.direction=self.randDirection()
        #根据方向获取图片
        self.image=self.images[self.direction]
        #区域
        self.rect=self.image.get_rect()
        #对left和top赋值
        self.rect.left=left
        self.rect.top=top
        #速度
        self.speed=speed
        #移动开关键
        self.flag=True
        #新增加一个步数变量  step
        self.step=60

    #随机生成敌方坦克的方向
    def randDirection(self):
        num=random.randint(1,4)
        if num == 1:
            return 'U'
        elif num == 2:
            return 'D'
        elif num == 3:
            return 'L'
        elif num == 4:
            return 'R'

    #敌方坦克随机移动的方法
    def randMove(self):
        if self.step<=0:
            #修改方向
            self.direction=self.randDirection()
            #让步数复位
            self.step=60
        else:
            self.move()
            #让步数递减
            self.step-=1

#子弹类
class Bullet():
    def __init__(self,tank):
        #加载图片
        self.imageU = pygame.image.load('image/bulletU.gif')
        self.imageD = pygame.image.load('image/bulletD.gif')
        self.imageL = pygame.image.load('image/bulletL.gif')
        self.imageR = pygame.image.load('image/bulletR.gif')
        #坦克的方向决定子弹的方向
        self.direction=tank.direction
        #获取区域
        self.rectU = self.imageU.get_rect()
        self.rectD = self.imageD.get_rect()
        self.rectL = self.imageL.get_rect()
        self.rectR = self.imageR.get_rect()
        #子弹的left和top与方向有关
        if self.direction == 'U':
            self.rectU.left=tank.rect.left+tank.rect.width/2-self.rectU.width/2
            self.rectU.top=tank.rect.top-self.rectU.height
        elif self.direction == 'D':
            self.rectD.left=tank.rect.left+tank.rect.width/2-self.rectD.width/2
            self.rectD.top=tank.rect.top+tank.rect.height
        elif self.direction == 'L':
            self.rectL.left=tank.rect.left-self.rectL.width/2-self.rectL.width/2
            self.rectL.top=tank.rect.top+tank.rect.width/2-self.rectL.width/2
        elif self.direction == 'R':
            self.rectR.left = tank.rect.left+tank.rect.width
            self.rectR.top = tank.rect.top + tank.rect.width / 2 - self.rectR.width / 2

        #子弹的速度
        self.speed=6



    #移动
    def move(self):
        pass

    #展示子弹的方法
    def displayBullet(self):
        #将图片surface加载到窗口
        MainGame.window.blit(self.imageU,self.rectU)
        MainGame.window.blit(self.imageD, self.rectD)
        MainGame.window.blit(self.imageL, self.rectL)
        MainGame.window.blit(self.imageR, self.rectR)


class Wall():
    def __init__(self):
        pass

    #展示墙壁的方法
    def displayWall(self):
        pass

class Explode():
    def __init__(self):
        pass
    #展示爆炸效果的方法
    def displayExplode(selfself):
        pass

class Music():
    def __init__(self):
        pass
    #播放音乐的方法
    def play(self):
        pass


if __name__ == "__main__":
    MainGame().startGame()