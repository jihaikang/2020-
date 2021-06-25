import pygame

pygame.init()

# 创建游戏的窗口 480 * 700
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1> 加载图像数据
bg = pygame.image.load("./images/background.png")
# 2> blit 绘制图像
# 加载图像到绘制的窗口上用的是对象screen
screen.blit(bg, (0, 0)) # 这里可不可以认为铺满窗口就是(0,0)，是这个图像原本就大，所以随便铺设
# 3> update 更新屏幕显示,用的是系统的pygame.display.update
pygame.display.update()

while True:
    pass

pygame.quit()
