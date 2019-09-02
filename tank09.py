"""
新增功能：
    优化：按下方向键，坦克一直移动
          松开方向键，坦克停止
"""
#导入pygame模块
import pygame,time

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BG_COLOR = pygame.Color(0,0,0)
TEXT_COLOR=pygame.Color(255,0,0)

class MainGame():
    window=None
    my_tank=None
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
            MainGame.window.blit(self.getTextSurface('敌方坦克剩余数量6'),(10,10))
            #调用坦克显示的方法
            MainGame.my_tank.displayTank()
            #调用移动方法
            #如果坦克的方向开关开启，才可以移动
            if not MainGame.my_tank.stop:
                MainGame.my_tank.move()
            pygame.display.update()

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
    def __init__(self):
        pass

#子弹类
class Bullet():
    def __init__(self):
        pass

    #移动
    def move(self):
        pass

    #展示子弹的方法
    def displayBullet(self):
        pass


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