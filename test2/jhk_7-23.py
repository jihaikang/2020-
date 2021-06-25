# 装饰器函数（使用装饰器和取消装饰器）
# 1.输出函数执行时间的装饰器

# def record_time(func):
#     '''自定义装饰函数的装饰器'''
#
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         start = time()
#         result = func(*args,**kwargs)
#         print(f'{func.__name__}:{time()- start}秒')
#         return wrapper
# 如果装饰器不希望跟print函数耦合，可以编写可以参数化的装饰器
# from functools import wraps
# from time import time
#
# def record(output):
#     '''可以参数化的装饰器'''
#
#     def decorate(func):
#
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             start = time()
#             result = func(*args,**kwargs)
#             output(func.__name__,time()-start)
#             return result
#
#         return  wrapper
#     return decorate()
# from functools import wraps
# from time import time
#
# class Record():
#     '''通过定义类的方式定义装饰器'''
#
#     def __init__(self,output):
#         self.output = output
#
#     def __call__(self,func):
#
#         @wraps(func)
#         def wrapper(*args,**kwargs):
#             start = time()
#             result = func(*args,**kwargs)
#             self.output(func.__name__,time()-start)
#             return result
#
#         return wrapper
# 用装饰器来实现单例模式
#
# from functools import wraps
#
# def singleton(cls):
#     '''装饰类的装饰器'''
#     instance = {}
#
#     @wraps(cls)
#     def wrapper(*args,**kwargs):
#         if cls not in instance:
#             instance[cls]=cls(*args,**kwargs)
#         return instance[cls]
#     return wrapper
#
# @singleton
# class President:
#     '''总统(单例类)'''
#     pass
# from functools import wraps
# from threading import RLock
#
# def singleton(cls):
#     '''线程安全的单例装饰器'''
#     instances = {}
#     locker = RLock()
#
#     @wraps(cls)
#     def wrapper(*args,**kwargs):
#         if cls not in instances:
#             with locker:
#                 if cls not in instances:
#                     instances[cls]=cls(*args,**kwargs)
#         return instances[cls]
#
#     return wrapper
'''
月薪结算系统 - 部门经理每月15000 程序员每小时200 销售员1800底薪加销售额5%提成
'''
# from abc import ABCMeta,abstractmethod
#
# class Employee(metaclass=ABCMeta):
#     '''员工（抽象类）'''
#
#     def __init__(self,name):
#         self.name = name
#
#     @abstractmethod
#     def get_salary(self):
#         '''结算月薪(抽象方法)'''
#         pass
#
# class Manger(Employee):
#     '''部门经理'''
#
#     def get_salary(self):
#         return 15000.0
#
# class Programmer(Employee):
#     '''程序员'''
#
#     def __init__(self,name,working_hour = 0):
#         self.working_hour = working_hour
#         super().__init__(name)
#
#     def get_salary(self):
#         return 200.0*self.working_hour
#
# class Salesman(Employee):
#     '''销售员'''
#
#     def __init__(self,name,sales = 0.0):
#         self.sales = sales
#         super().__init__(name)
#
#     def get_salary(self):
#         return 1800.00 + self.sales * 0.05
#
# class EmployeeFactor:
#     '''创建员工的工厂(工厂模式 - 通过工厂实现对象使用者和对象之间的解耦合)'''
#
#     @staticmethod
#     def create(emp_type,*args,**kwargs):
#         '''创建员工'''
#         all_emp_types = {'M':Manger,'P':Programmer,'S':Salesman}
#         cls = all_emp_types[emp_type.upper()]
#         return cls(*args,**kwargs) if cls else None
#
# def main():
#     '''主函数'''
#     emps = [
#         EmployeeFactor.create('M','曹操'),
#         EmployeeFactor.create('P','荀彧',120),
#         EmployeeFactor.create('P','郭嘉',85),
#         EmployeeFactor.create('S','典韦',123000)
#     ]
#     for emp in emps:
#         print(f'{emp.name}:{emp.get_salary():.2f}元')
#
# if __name__ == '__main__':
#     main()
# 扑克游戏
'''
经验：符号常量总是优于字面常量，枚举类型是定义符号常量的最佳选择
'''
from enum import Enum,unique

import random

@unique
class Suite(Enum):
    '''花色'''

    SPADE,HEART,CLUB,DIAMOND = range(4)

    def __lt__(self, other):
        return self.value < other.value

class Card():
    '''牌'''

    def __init__(self,suite,face):
        '''初始化方法'''
        self.suite = suite
        self.face = face

    def show(self):
        """显示牌面"""
        suites = ['♠︎', '♥︎', '♣︎', '♦︎']
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'

    def __repr__(self):
        return self.show()

class Poker():
    """扑克"""

    def __init__(self):
        self.index = 0
        self.cards = [Card(suite, face)
                      for suite in Suite
                      for face in range(1, 14)]

    def shuffle(self):
        """洗牌（随机乱序）"""
        random.shuffle(self.cards)
        self.index = 0

    def deal(self):
        """发牌"""
        card = self.cards[self.index]
        self.index += 1
        return card

    @property
    def has_more(self):
        return self.index < len(self.cards)

class Player():
    """玩家"""

    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_one(self, card):
        """摸一张牌"""
        self.cards.append(card)

    def sort(self, comp=lambda card: (card.suite, card.face)):
        """整理手上的牌"""
        self.cards.sort(key=comp)

def main():
    """主函数"""
    poker = Poker()
    poker.shuffle()
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
    while poker.has_more:
        for player in players:
            player.get_one(poker.deal())
    for player in players:
        player.sort()
        print(player.name, end=': ')
        print(player.cards)

if __name__ == '__main__':
    main()
