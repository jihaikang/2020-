# import tkinter
# import tkinter.messagebox
#
#
# def main():
#     flag =True
#
#     # 修改标签上的文字
#     def change_label_text():
#         nonlocal flag
#         flag = not flag
#         color , msg = ('red','hello,,world!')\
#             if flag else ('blue','Goodbye,world!')
#         label.config(text=msg, fg=color)
#
#         # 确认退出
#     def confirm_to_quit():
#         if tkinter.messagebox.askokcancel('温馨提示','确定要退出么?'):
#             top.quit()
#
#     # 创建顶层窗口
#     top = tkinter.Tk()
#      # 设置窗口大小
#     top.geometry('240x160')
#     # 设置窗口标题
#     top.title('小游戏')
#     # 创建标签对象并添加到顶层窗口
#     label = tkinter.Label(top, text = 'hello')
#     label.pack(expand = 1)
#     # 创建一个装按钮的容器
#     panel = tkinter.Frame(top)
#     # 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
#     button1 = tkinter.Button(panel , text = '修改',command = change_label_text())
#     button1.pack(side = 'left')
#     button2 = tkinter.Button(panel, text='退出',command=confirm_to_quit())
#     button2.pack(side='right')
#     panel.pack(side='bottom')
#     # 开启主事件循环
#     tkinter.mainloop()
#
# if __name__ == '__main__':
#     main()
# 制作游戏窗口
# import  pygame
#
# def main():
#     # 初始化导入的pygame中的模块
#     pygame.init()
#     # 初始化用于显示的窗口并设置窗口尺寸
#     screen = pygame.display.set_mode((800,600))
#     # 设置当前窗口标题
#     pygame.display.set_caption('大球吃小球')
#     running = True
#     # 开启一个事件循环处理发生的事件
#     while running:
#         # 从消息队列中获取事件并对事件进行处理
#         for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     running = False
#
# if __name__ == '__main__':
#     main()
# 在窗口中绘图
# import pygame
#
# def main():
#     # 初始化导入的pygame中的模块
#     pygame.init()
#     # 初始化用于显示的窗口并设置窗口尺寸
#     screen = pygame.display.set_mode((800,600))
#     # 设置当前窗口的标题
#     pygame.display.set_caption('大球吃小球')
#     # 设置窗口的背景色（颜色是由红绿蓝三原色构成的元组）
#     screen.fill((242,242,242))
#     # 绘制一个圆（参数分别是：屏幕，颜色，圆心位置，半径，0表示填充圆）
#     pygame.draw.circle(screen,(255,12,34),(100,100),30,0)
#     # 刷新当前窗口（渲染窗口将绘制的图像呈现出来）
#     pygame.display.flip()
#     running =True
#     # 开启一个事件循环处理发生的事件
#     while running:
#         # 从消息队列中获取事件并对事件进行处理
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#
# if __name__ == '__main__':
#     main()
# import pygame
#
#
# def main():
#     # 初始化导入的pygame中的模块
#     pygame.init()
#     # 初始化用于显示的窗口并设置窗口尺寸
#     screen = pygame.display.set_mode((800, 600))
#     # 设置当前窗口的标题
#     pygame.display.set_caption('大球吃小球')
#     # 设置窗口的背景色(颜色是由红绿蓝三原色构成的元组)
#     screen.fill((255, 255, 255))
#     # 通过指定的文件名加载图像
#     ball_image = pygame.image.load('./ball.png')
#     # 在窗口上渲染图像
#     screen.blit(ball_image, (50, 50))
#     # 刷新当前窗口(渲染窗口将绘制的图像呈现出来)
#     pygame.display.flip()
#     running = True
#     # 开启一个事件循环处理发生的事件
#     while running:
#         # 从消息队列中获取事件并对事件进行处理
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#
#
# if __name__ == '__main__':
#     main()
# import pygame
#
# def main():
#     # 初始化导入的pygame中的模块
#     pygame.init()
#     # 初始化用于显示的窗口并设置窗口尺寸
#     screen = pygame.display.set_mode((800,600))
#     # 设置当前窗口的标题
#     pygame.display.set_caption('大球吃小球')
#     # 定义变量来表示小球在屏幕上的位置
#     x,y = 50,50
#     running = True
#     # 开启一个事件循环处理发生的事件
#     while running:
#         # 从消息队列中获取事件并对事件进行处理
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#
#         screen.fill((255,255,255))
#         pygame.draw.circle(screen,(255,0,0,),(x,y ),30,0)
#         pygame.display.flip()
#         pygame.time.delay(50)
#         x,y = x + 5,y +5
#
#
# if __name__ == '__main__':
#     main()
# from enum import Enum, unique
# from math import sqrt
# from random import randint
#
# import pygame
#
# @unique
# class Color(Enum):
#     '''颜色'''
#
#     RED = (255, 0, 0)
#     GREEN = (0, 255, 0)
#     BLUE = (0, 0, 255)
#     BLACK = (0, 0, 0)
#     WHITE = (255, 255, 255)
#     GRAY = (242, 242, 242)
#
#     @staticmethod
#     def random_color():
#         '''获得随机颜色'''
#         r = randint(0, 255)
#         g = randint(0, 255)
#         b = randint(0, 255)
#         return (r, g, b)
#
# class Ball(object):
#     '''球'''
#
#     def __init__(self,x,y,radius,sx,sy,color=Color.RED):
#         '''初始化方法'''
#         self.x = x
#         self.y = y
#         self.radius = radius
#         self.sx = sx
#         self.sy = sy
#         self.color = color
#         self.alive = True
#
#     def move(self,screen):
#         '''移动'''
#         self.x += self.sx
#         self.y += self.sy
#         if self.x - self.radius <= 0 or \
#             self.y +self.radius >= screen.get_width():
#             self.sx = -self.sx
#         if self.y - self.radius <= 0 or \
#             self.y + self.radius >= screen.get_width():
#             self.sy = -self.sy
#
#     def eat(self,other):
#             '''吃其他球'''
#             if self.alive and other.alive and self !=other:
#                 dx,dy = self.x - other.x,self.y - other.y
#                 distance = sqrt(dx ** 2 + dy ** 2)
#                 if distance <= self.radius +other.radius \
#                     and self.radius > other.radius:
#                     other.alive = False
#                     self.radius = self.radius + int(other.radius * 0.146)
#
#     def draw(self,screen):
#          '''在窗口绘制球'''
#          pygame.draw.circle(screen,self.color,
#                             (self.x, self.y), self.radius, 0)
#
#
# def main():
#     # 定义用来装所有球的容器
#     balls = []
#     # 初始化导入的pygame中的模块
#     pygame.init()
#     # 初始化用于显示的窗口并设置窗口尺寸
#     screen = pygame.display.set_mode((800,600))
#     # 设置当前窗口的标题
#     pygame.display.set_caption('大球吃小球')
#     running = True
#     # 开启一个事件循环处理发生的事件
#     while running:
#         # 从消息队列中获取事件并对事件进行粗粒
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             # 处理鼠标事件的代码
#             if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#                 # 获得点击鼠标的位置
#                 x, y = event.pos
#                 radius = randint(10, 20)
#                 sx, sy = randint(-10,10), randint(-10,10)
#                 color = Color.random_color()
#                 # 在点击鼠标的位置创建一个球（大小、速度和颜色随机）
#                 ball = Ball(x, y, radius, sx, sy, color)
#                 # 将球添加到列表容器中
#                 balls.append(ball)
#         screen.fill((255,255,255))
#         # 取出容器中的球 如果没被吃掉就绘制 被吃掉就移除
#         for ball in balls:
#             if ball.alive:
#                 ball.draw(screen)
#             else:
#                 balls.remove(ball)
#         pygame.display.flip()
#          # 每隔20毫秒就改变球的位置再刷新窗口
#         pygame.time.delay(50)
#         for ball in balls:
#             ball.move(screen)
#             # 检查球没有吃到其他球
#             for other in balls:
#                 ball.eat(other)
#
#
# if __name__ == '__main__':
#     main()
# def main():
#     f = None
#     try:
#         f = open('D:\电子书\C语言经典书籍\c.txt','r',encoding='utf-8')
#         print(f.read())
#     except FileNotFoundError:
#         print('无法打开指定的文件！')
#     except LookupError:
#         print('指定了未知的编码！')
#     except UnicodeDecodeError:
#         print('读取文件时解码错误！')
#     finally:
#         if f:
#             f.close()
#
#
# if __name__ == '__main__':
#     main()
# # 上下文语法
# def main():
#     try:
#         with open('D:\电子书\C语言经典书籍\c.txt','r',encoding='utf-8') as f:
#             print(f.read())
#     except FileNotFoundError:
#         print('无法打开指定的文件！')
#     except LookupError:
#         print('指定了未知的编码！')
#     except UnicodeDecodeError:
#         print('读取文件时解码错误！')
#
#
# if  __name__ == '__main__':
#     main()
# c除了用文件对象的read方法读取文件之外
# 还可以试用for-in循环逐行读取或者
# 用 readlines方法将文件按行读取到一个列表容器中
# import time
#
# def main():
#     # 一次性读取整个文件内容
#     with open('D:\电子书\C语言经典书籍\cpple.txt','r',encoding='utf-8') as f:
#         print(f.read())
#
#     # 通过for-in循环逐行读取
#     with open('D:\电子书\C语言经典书籍\cpple.txt','r',encoding='utf-8') as f:
#         for line in f:
#             print(line, end="")
#             time.sleep(0.5)
#     print()
#
#
#     # 读取文件按行读取到列表中
#     with open('D:\电子书\C语言经典书籍\cpple.txt','r',encoding='utf-8') as f:
#         lines = f.readlines()
#         print(lines)
#
#
# if __name__ == '__main__':
#     main()
# 写入文件
# 将1-9999之间的素数分别写入三个文件中
# from math import sqrt
#
# def is_prime(n):
#     '''判断素数的函数'''
#     assert n > 0
#     for factor in range(2,int(sqrt(n)+1)):
#         if n % factor == 0:
#             return False
#     return  True if n != 1 else False
#
# def main():
#     filenames = ('a.txt','b.txt','c.txt')
#     fs_list = []
#     try:
#         for filename in filenames:
#             fs_list.append(open(filename,'w',encoding='utf-8'))
#         for number in range(1,10000):
#             if is_prime(number):
#                 if number <100:
#                     fs_list[0].write(str(number) + '\n')
#                 elif number <1000:
#                     fs_list[1].write(str(number) + '\n')
#                 else:
#                     fs_list[2].write(str(number)+ '\n')
#     except IOError as ex:
#         print(ex)
#         print('写文件时发生错误')
#     finally:
#         for fs in fs_list:
#             fs.close
#     print('操作完成')
#
# if __name__ == '__main__':
#     main()
# def main():
#     try:
#         with open('cb008e9d0f832a1be148b033a538d573.jpg','rb') as fs1:
#             data = fs1.read()
#             print(type(data)) #<class 'bytes'>
#         with open('d90392de6456ce7d54248132b3ccca81.jpg','wb') as fs2:
#             fs2.write(data) # 复制图像（利用二进制文件）
#     except FileNotFoundError as e:
#         print('指定的文件无法打开')
#     except IOError as e:
#         print('读写文件时出现错误')
#     print('程序执行结束')
#
#
# if __name__ == '__main__':
#     main()
# import json
#
#
# def main():
#     mydict = {
#         'name':'小白',
#         'age':21,
#         'qq': 123456,
#         'friends': ['王大锤', '李元芳'],
#         'cars': [
#             {'brand': 'BYD','max_speed': 180},
#             {'brand': 'Audi','max_speed': 280},
#             {'brand':'Benz','max_speed': 320}
#             ]
#     }
#     try:
#         with open('data.json','w',encoding='utf-8') as fs:
#             json.dump(mydict,fs)
#     except IOError as e:
#         print(e)
#     print('保存数据完成！')
#
#
# if __name__ == '__main__':
#     main()
# import requests
# import json
#
#
# def main():
#     resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10') # api接口已失效
#     data_model = json.loads(resp.text)
#     for news in data_model['newslist']:
#         print(news['title'])
#
#
# if __name__ == '__main__':
#     main()
# 验证输入用户名和QQ号是否有效并给出对应的提示消息
'''
验证输入用户名和QQ号是否有效并给出对应的提示信息

要求：用户名必须由字母、数字或下划线构成且长度在6-20个字符之间,QQ号是5-12的数字且首位不能为0
'''
# import re
#
# def main():
#     username = input('请输入用户名：')
#     qq = input('请输入QQ号：')
#     # match函数的第一个参数是正则表达式字符串或正则表达式对象
#     # 第二个参数是要跟正则表达式做匹配的字符串对象
#     m1 = re.match(r'^[0-9a-zA-Z]{6,20}$',username)
#     if not m1:
#         print('请输入有效的用户名。')
#     m2 = re.match(r'^[1-9]\d{4,11}$', qq)
#     if not m2:
#         print('请输入有效的QQ号.')
#     if m1 and m2:
#         print('你输入的信息是有效的！')
#
# if __name__ == '__main__':
#     main()
# 从一段文字中提取出国内手机号码

# import re
#
# def main():
#     # 创建正则表达式对象 使用了前瞻和回顾来保证手机号前好不应该出现数字
#     pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
#     sentence = '''
#     重要的事情说8130123456789遍，我的手机号是135123456789这个靓号,
#     不是15600998765，也不是110或119，王大锤的手机号才是15600998765
#     '''
#     # 查找所有匹配并保存到一个列表中
#     mylist = re.findall(pattern, sentence)
#     print(mylist)
#     print('-------华丽的分割线-------')
#     # 通过迭代器取出匹配对象并获得匹配的内容
#     for temp in pattern.finditer(sentence):
#         print(temp.group)
#     print('--------华丽的分割线--------')
#     #通过search函数指定搜索位置找出所有匹配
#     m = pattern.search(sentence)
#     while m:
#         print(m.group())
#         m = pattern.search(sentence,m.end())
#
#
# if __name__ == '__main__':
#     main()
# 替换字符串中的不良内容
# import re
#
# def main():
#     sentence = '你丫是傻叉么？我操你大爷的.Fuck you.'
#     purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔', '*', sentence, flags=re.IGNORECASE)
#     print(purified) # 你丫是*吗? 我*你大爷的. * you.
#
#
# if __name__ == '__main__':
#     main()
# 拆分长字符串

import re


def main():
    poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[，。，。]',poem)
    while ''in sentence_list:
        sentence_list.remove('')
        print(sentence_list)


if __name__ =='__main__':
    main()