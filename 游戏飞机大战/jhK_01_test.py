import pygame
from plane_sprites import *

pygame.init()
pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
clock = pygame.time.Clock
i = 0
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1> 加载图像
bg = pygame.image.load("./images/background.png")

# 2> 绘制在屏幕
screen.blit(bg, (0, 0))
hero = pygame.image.load("./images/me1.png")

screen.blit(hero, (200, 500))
hero_rect = pygame.Rect(150, 500, 102, 126)
# 3>

# 创建敌机精灵和精灵组
enemy1 = GameSprite("./images/enemy1.png")
enemy2 = GameSprite("./images/enemy1.png", 2)
enemy2.rect.x = 200
enemy_group = pygame.sprite.Group(enemy1, enemy2)

pygame.display.update()


while True:

    # 可以指定循环体内部的代码执行的频率


    # 更新英雄位置
    hero_rect.y -= 1
    enemy_group.update()
    enemy_group.draw(screen)
    for event in pygame.event.get():

        # 判断用户是否点击了关闭按钮
        if event.type == pygame.QUIT:
            print("退出游戏...")

    # 如果移出屏幕，则将英雄的顶部移动到屏幕底部
    if hero_rect.y <= 0:
        hero_rect.y = 700

    # 绘制背景图片
    screen.blit(bg, (0, 0))
    # 绘制英雄图像
    screen.blit(hero, hero_rect)


    # 更新显示
    pygame.display.update()



