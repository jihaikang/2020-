# import os
# import time
#
#
# def main():
#     content = '北京欢迎你为你开天辟地…………'
#     while True:
#         # 清理屏幕上的输出
#         os.system('cls')  # os.system('clear')
#         print(content)
#         # 休眠200毫秒
#         time.sleep(0.2)
#         content = content[1:] + content[0]
#
#
# if __name__ == '__main__':
#     main()
# import random
#
#
# def generate_code(code_len):
#     """
#     生成指定长度的验证码
#
#     :param code_len: 验证码的长度(默认4个字符)
#
#     :return: 由大小写英文字母和数字构成的随机验证码
#     """
#     all_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     last_pos = len(all_chars) - 1
#     code = ''
#     for _ in range(code_len):
#         index = random.randint(0, last_pos)
#         code += all_chars[index]
#     print(code)
#
# generate_code(2)
# def get_suffix(filename, has_dot=False):
#     """
#     获取文件名的后缀名
#
#     :param filename: 文件名
#     :param has_dot: 返回的后缀名是否需要带点
#     :return: 文件的后缀名
#     """
#     pos = filename.rfind('.') # rfind从右向左查 ， find 从左向右查
#     if 0 < pos < len(filename) - 1: # 思路找出文件名的点，并由点来确定索引为位置，前提文件名所在的存储空间可以有索引
#         index = pos if has_dot else pos + 1
#         return filename[index:]
#     else:
#         return ''
# from time import sleep
#
#
# class Clock(object):
#     """数字时钟"""
#
#     def __init__(self, hour=0, minute=0, second=0):
#         """初始化方法
#
#         :param hour: 时
#         :param minute: 分
#         :param second: 秒
#         """
#         self._hour = hour
#         self._minute = minute
#         self._second = second
#
#     def run(self):
#         """走字"""
#         self._second += 1
#         if self._second == 60:
#             self._second = 0
#             self._minute += 1
#             if self._minute == 60:
#                 self._minute = 0
#                 self._hour += 1
#                 if self._hour == 24:
#                     self._hour = 0
#
#     def show(self):
#         """显示时间"""
#         return '%02d:%02d:%02d' % \
#                (self._hour, self._minute, self._second)
#
#
# def main():
#     clock = Clock(23, 59, 58)
#     while True:
#         print(clock.show())
#         sleep(1)
#         clock.run()
#
#
# if __name__ == '__main__':
#     main()
# from math import sqrt
#
#
# class Point(object):
#     def __init__(self, x=0, y=0):
#         """初始化方法
#
#         :param x: 横坐标
#         :param y: 纵坐标
#         """
#         self.x = x
#         self.y = y
#
#     def move_to(self, x, y):
#         """移动到指定位置
#
#         :param x: 新的横坐标
#         "param y: 新的纵坐标
#         """
#         self.x = x
#         self.y = y
#
#     def move_by(self, dx, dy):
#         """移动指定的增量
#
#         :param dx: 横坐标的增量
#         "param dy: 纵坐标的增量
#         """
#         self.x += dx
#         self.y += dy
#
#     def distance_to(self, other):
#         """计算与另一个点的距离
#
#         :param other: 另一个点
#         """
#         dx = self.x - other.x
#         dy = self.y - other.y
#         return sqrt(dx ** 2 + dy ** 2)
#
#     def __str__(self):
#         return '(%s, %s)' % (str(self.x), str(self.y))#"""返回一个对象的描述信息"""
#
#
# def main():
#     p1 = Point(3, 5)
#     p2 = Point()
#     print(p1)
#     print(p2)
#     p2.move_by(-1, 2)
#     print(p2)
#     print(p1.distance_to(p2))
#
#
# if __name__ == '__main__':
#     main()
# from math import sqrt
#
#
# class Triangle(object):
#
#     def __init__(self, a, b, c):
#         self._a = a
#         self._b = b
#         self._c = c
#
#     @staticmethod # 静态方法
#     def is_valid(a, b, c):
#         return a + b > c and b + c > a and a + c > b
#
#     def perimeter(self):
#         return self._a + self._b + self._c
#
#     def area(self):
#         half = self.perimeter() / 2
#         return sqrt(half * (half - self._a) *
#                     (half - self._b) * (half - self._c))
#
#
# def main():
#     a, b, c = 3, 4, 5
#     # 静态方法和类方法都是通过给类发消息来调用的
#     if Triangle.is_valid(a, b, c):
#         t = Triangle(a, b, c)
#         print(t.perimeter())
#         # 也可以通过给类发消息来调用对象方法但是要传入接收消息的对象作为参数
#         # print(Triangle.perimeter(t))
#         print(t.area())
#         # print(Triangle.area(t))
#     else:
#         print('无法构成三角形.')
# #
#
# if __name__ == '__main__':
#     main()
# from abc import ABCMeta, abstractmethod
# from random import randint, randrange
#
#
# class Fighter(object, metaclass=ABCMeta):
#     """战斗者"""
#
#     # 通过__slots__魔法限定对象可以绑定的成员变量
#     __slots__ = ('_name', '_hp')
#
#     def __init__(self, name, hp):
#         """初始化方法
#
#         :param name: 名字
#         :param hp: 生命值
#         """
#         self._name = name
#         self._hp = hp
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def hp(self):
#         return self._hp
#
#     @hp.setter
#     def hp(self, hp):
#         self._hp = hp if hp >= 0 else 0
#
#     @property
#     def alive(self):
#         return self._hp > 0
#
#     @abstractmethod
#     def attack(self, other):
#         """攻击
#
#         :param other: 被攻击的对象
#         """
#         pass
#
#
# class Ultraman(Fighter):
#     """奥特曼"""
#
#     __slots__ = ('_name', '_hp', '_mp')
#
#     def __init__(self, name, hp, mp):
#         """初始化方法
#
#         :param name: 名字
#         :param hp: 生命值
#         :param mp: 魔法值
#         """
#         super().__init__(name, hp)
#         self._mp = mp
#
#     def attack(self, other):
#         other.hp -= randint(15, 25)
#
#     def huge_attack(self, other):
#         """究极必杀技(打掉对方至少50点或四分之三的血)
#
#         :param other: 被攻击的对象
#
#         :return: 使用成功返回True否则返回False
#         """
#         if self._mp >= 50:
#             self._mp -= 50
#             injury = other.hp * 3 // 4
#             injury = injury if injury >= 50 else 50
#             other.hp -= injury
#             return True
#         else:
#             self.attack(other)
#             return False
#
#     def magic_attack(self, others):
#         """魔法攻击
#
#         :param others: 被攻击的群体
#
#         :return: 使用魔法成功返回True否则返回False
#         """
#         if self._mp >= 20:
#             self._mp -= 20
#             for temp in others:
#                 if temp.alive:
#                     temp.hp -= randint(10, 15)
#             return True
#         else:
#             return False
#
#     def resume(self):
#         """恢复魔法值"""
#         incr_point = randint(1, 10)
#         self._mp += incr_point
#         return incr_point
#
#     def __str__(self):
#         return '~~~%s奥特曼~~~\n' % self._name + \
#             '生命值: %d\n' % self._hp + \
#             '魔法值: %d\n' % self._mp
#
#
# class Monster(Fighter):
#     """小怪兽"""
#
#     __slots__ = ('_name', '_hp')
#
#     def attack(self, other):
#         other.hp -= randint(10, 20)
#
#     def __str__(self):
#         return '~~~%s小怪兽~~~\n' % self._name + \
#             '生命值: %d\n' % self._hp
#
#
# def is_any_alive(monsters):
#     """判断有没有小怪兽是活着的"""
#     for monster in monsters:
#         if monster.alive > 0:
#             return True
#     return False
#
#
# def select_alive_one(monsters):
#     """选中一只活着的小怪兽"""
#     monsters_len = len(monsters)
#     while True:
#         index = randrange(monsters_len)
#         monster = monsters[index]
#         if monster.alive > 0:
#             return monster
#
#
# def display_info(ultraman, monsters):
#     """显示奥特曼和小怪兽的信息"""
#     print(ultraman)
#     for monster in monsters:
#         print(monster, end='')
#
#
# def main():
#     u = Ultraman('骆昊', 1000, 120)
#     m1 = Monster('狄仁杰', 250)
#     m2 = Monster('白元芳', 500)
#     m3 = Monster('王大锤', 750)
#     ms = [m1, m2, m3]
#     fight_round = 1
#     while u.alive and is_any_alive(ms):
#         print('========第%02d回合========' % fight_round)
#         m = select_alive_one(ms)  # 选中一只小怪兽
#         skill = randint(1, 10)   # 通过随机数选择使用哪种技能
#         if skill <= 6:  # 60%的概率使用普通攻击
#             print('%s使用普通攻击打了%s.' % (u.name, m.name))
#             u.attack(m)
#             print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
#         elif skill <= 9:  # 30%的概率使用魔法攻击(可能因魔法值不足而失败)
#             if u.magic_attack(ms):
#                 print('%s使用了魔法攻击.' % u.name)
#             else:
#                 print('%s使用魔法失败.' % u.name)
#         else:  # 10%的概率使用究极必杀技(如果魔法值不足则使用普通攻击)
#             if u.huge_attack(m):
#                 print('%s使用究极必杀技虐了%s.' % (u.name, m.name))
#             else:
#                 print('%s使用普通攻击打了%s.' % (u.name, m.name))
#                 print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
#         if m.alive > 0:  # 如果选中的小怪兽没有死就回击奥特曼
#             print('%s回击了%s.' % (m.name, u.name))
#             m.attack(u)
#         display_info(u, ms)  # 每个回合结束后显示奥特曼和小怪兽的信息
#         fight_round += 1
#     print('\n========战斗结束!========\n')
#     if u.alive > 0:
#         print('%s奥特曼胜利!' % u.name)
#     else:
#         print('小怪兽胜利!')
#
#
# if __name__ == '__main__':
#     main()
# # def main():
# #     try:
# #         with open('致橡树.txt', 'r', encoding='utf-8') as f:
# #             print(f.read())
# #     except FileNotFoundError:
# #         print('无法打开指定的文件!')
# #     except LookupError:
# #         print('指定了未知的编码!')
# #     except UnicodeDecodeError:
# #         print('读取文件时解码错误!')
# #
# #
# # if __name__ == '__main__':
# #     main()
# from math import sqrt
#
#
# def is_prime(n):
#     """判断素数的函数"""
#     assert n > 0
#     for factor in range(2, int(sqrt(n)) + 1):
#         if n % factor == 0:
#             return False
#     return True if n != 1 else False
#
#
# def main():
#     filenames = ('a.txt', 'b.txt', 'c.txt')
#     fs_list = []
#     try:
#         for filename in filenames:
#             fs_list.append(open(filename, 'w', encoding='utf-8'))
#         for number in range(1, 10000):
#             if is_prime(number):
#                 if number < 100:
#                     fs_list[0].write(str(number) + '\n')
#                 elif number < 1000:
#                     fs_list[1].write(str(number) + '\n')
#                 else:
#                     fs_list[2].write(str(number) + '\n')
#     except IOError as ex:
#         print(ex)
#         print('写文件时发生错误!')
#     finally:
#         for fs in fs_list:
#             fs.close()
#     print('操作完成!')
#
#
# if __name__ == '__main__':
#     main()
#     main()
# {
#     "name": "骆昊",
#     "age": 38,
#     "qq": 957658,
#     "friends": ["王大锤", "白元芳"],
#     "cars": [
#         {"brand": "BYD", "max_speed": 180},
#         {"brand": "Audi", "max_speed": 280},
#         {"brand": "Benz", "max_speed": 320}
#     ]
# }
# from socket import socket
# from json import loads
# from base64 import b64decode
# #
# #
# def main():
#     client = socket()
#     client.connect(('192.168.0.100', 5566))
#     # 定义一个保存二进制数据的对象
#     in_data = bytes()
#     # 由于不知道服务器发送的数据有多大每次接收1024字节
#     data = client.recv(1024)
#     while data:
#         # 将收到的数据拼接起来
#         in_data += data
#         data = client.recv(1024)
#     # 将收到的二进制数据解码成JSON字符串并转换成字典
#     # loads函数的作用就是将JSON字符串转成字典对象
#     my_dict = loads(in_data.decode('utf-8'))
#     filename = my_dict['filename']
#     filedata = my_dict['filedata'].encode('utf-8')
#     with open('/Users/Hao/' + filename, 'wb') as f:
#         # 将base64格式的数据解码成二进制数据并写入文件
#         f.write(b64decode(filedata))
#     print('图片已保存.')
# #
# #
# if __name__ == '__main__':
#     main()
# from smtplib import SMTP
#
# from email.header import Header
# from email.mime.text import MIMEText


# def main():
#     # 请自行修改下面的邮件发送者和接收者
#     sender = '24156479012@qq.com'
#     receivers = ['2993431608@qq.com', '2993431608@qq.com']
#     message = MIMEText('用Python发送邮件的示例代码.', 'plain', 'utf-8')
#     message['From'] = Header('王大锤', 'utf-8')
#     message['To'] = Header('骆昊', 'utf-8')
#     message['Subject'] = Header('示例代码实验邮件', 'utf-8')
#     smtper = SMTP('smtp.126.com')
#     # 请自行修改下面的登录口令
#
#     smtper.login(sender, 'secretpass')
#     smtper.sendmail(sender, receivers, message.as_string())
#     print('邮件发送完成!')

#   以下本机需本机安装sendmail
# sender = 'from@runoob.com'
# receivers = ['2993431608@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
#
# # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
# message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
# message['From'] = Header("菜鸟教程", 'utf-8')  # 发送者
# message['To'] = Header("测试", 'utf-8')  # 接收者
#
# subject = 'Python SMTP 邮件测试'
# message['Subject'] = Header(subject, 'utf-8')
#
# try:
#     smtpObj = smtplib.SMTP('localhost')
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print("邮件发送成功")
# except smtplib.SMTPException:
#     print("Error: 无法发送邮件")

#
#
# if __name__ == '__main__':
#     main()
# class Thing(object):
#     """物品"""
# #
#     def __init__(self, name, price, weight):
#         self.name = name
#         self.price = price
#         self.weight = weight
#
#     @property
#     def value(self):
#         """价格重量比"""
#         return self.price / self.weight
#
#
# def input_thing():
#     """输入物品信息"""
#     name_str, price_str, weight_str = input().split()
#     return name_str, int(price_str), int(weight_str)
#
#
# def main():
#     """主函数"""
#     max_weight, num_of_things = map(int, input().split())
#     all_things = []
#     for _ in range(num_of_things):
#         all_things.append(Thing(*input_thing()))
#     all_things.sort(key=lambda x: x.value, reverse=True)
#     total_weight = 0
#     total_price = 0
#     for thing in all_things:
#         if total_weight + thing.weight <= max_weight:
#             print(f'小偷拿走了{thing.name}')
#             total_weight += thing.weight
#             total_price += thing.price
#     print(f'总价值: {total_price}美元')
#
#
# if __name__ == '__main__':
#     main()
# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration
#
#
# myclass = MyNumbers()
# myiter = iter(myclass)
#
# for x in myiter:
#     print(x,end=" ")