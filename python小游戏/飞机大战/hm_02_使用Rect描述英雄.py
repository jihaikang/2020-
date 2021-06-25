import pygame

hero_rect = pygame.Rect(100, 500, 120, 125) # pygame.Rect(x,y,width,height)

print("英雄的原点 %d %d" % (hero_rect.x, hero_rect.y))
print("英雄的尺寸 %d %d" % (hero_rect.width, hero_rect.height))
print("%d %d" % hero_rect.size) # size表示的是绘制框架的宽与高
