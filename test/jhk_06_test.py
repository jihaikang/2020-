# def demo(num, num_list):
#
#     print("函数内部")
#
#     # 赋值语句
#     num = 200
#     num_list = [1, 2, 3]
#
#     print(num)
#     print(num_list)
#
#     print("函数代码完成")
#
#
# gl_num = 99
# gl_list = [4, 5, 6]
# demo(gl_num, gl_list)
# print(gl_num)
# print(gl_list)
#
#
# def mutable(num_list):
#     # num_list = [1, 2, 3]
#     num_list.extend([1, 2, 3])
#
#     print(num_list)
#
#
# gl_list = [6, 7, 8]
# mutable(gl_list)
# print(gl_list)
#
#
# # def measure():
# #     """返回当前的温度"""
# #
# #     print("开始测量...")
# #     temp = 39
# #     print("测量结束...")
# #
# #     print(temp)
# #
# # measure()
# def measure():
#     """返回当前的温度"""
#
#     print("开始测量...")
#     temp = 39
#     wetness = 10
#     print("测量结束...")
#
#     return (temp, wetness)
# a , temp =b = measure()
# print(measure())
# def demo(num, num_list):
#
#     print("函数内部代码")
#
#     # num = num + num
#     num += num
#     # num_list.extend(num_list) 由于是调用方法，所以不会修改变量的引用
#     # 函数执行结束后，外部数据同样会发生变化
#     num_list += num_list
#
#     print(num)
#     print(num_list)
#     print("函数代码完成")
#
#
# gl_num = 9
# gl_list = [1, 2, 3]
# demo(gl_num, gl_list)
# print(gl_num)
# print(gl_list)
#
#
# gl_num_list = [6, 3, 9]
#
# # 默认就是升序排序，因为这种应用需求更多
# gl_num_list.sort()
# print(gl_num_list)
#
# # 只有当需要降序排序时，才需要传递 `reverse` 参数
# gl_num_list.sort(reverse=True)
# print(gl_num_list)
# def print_info(name, gender=True):
#
#     gender_text = "男生"
#     if not gender:
#         gender_text = "女生"
#
#     print("%s 是 %s" % (name, gender_text))
# print_info('小明','')
# def print_info(name, title="", gender=True):
#     """
#
#     :param title: 职位
#     :param name: 班上同学的姓名
#     :param gender: True 男生 False 女生
#     """
#
#     gender_text = "男生"
#
#     if not gender:
#         gender_text = "女生"
#
#     print("%s%s 是 %s" % (title, name, gender_text))
#
#
# # 提示：在指定缺省参数的默认值时，应该使用最常见的值作为默认值！
# print_info("小明")
# print_info("老王", title="班长")
# print_info("小美", gender=False)
# def demo(num, *args, **kwargs):
#
#     print(num)
#     print(args)
#     print(kwargs)
#
#
# demo(1, 2, 3, 4, 5, name="小明", age=18, gender=True)
# def sum_numbers(*args):
#
#     num = 0
#     # 遍历 args 元组顺序求和
#     for n in args:
#         num += n
#
#     return num
#
# print(sum_numbers(1,3,4))
# def demo(*args, **kwargs):
#
#     print(args)
#     print(kwargs)
#
#
# # 需要将一个元组变量/字典变量传递给函数对应的参数
# gl_nums = (1, 2, 3)
# gl_xiaoming = {"name": "小明", "age": 18}
#
# # 会把 num_tuple 和 xiaoming 作为元组传递个 args
# # demo(gl_nums, gl_xiaoming)
# demo(*gl_nums, **gl_xiaoming)


# def sum_numbers(num):
#     print(num)
#
#     # 递归的出口很重要，否则会出现死循环
#     if num == 1:
#         return
#
#     sum_numbers(num - 1)
#
#
# sum_numbers(3)
# def sum_numbers(num):
#     if num == 1:
#         return 1
#
#     # 假设 sum_numbers 能够完成 num - 1 的累加
#     temp = sum_numbers(num - 1)
#
#     # 函数内部的核心算法就是 两个数字的相加
#     return num + temp
#
#
# print(sum_numbers(4))
# class Cat:
#
#     def __init__(self, new_name):
#
#         self.name = new_name
#
#         print("%s 来了" % self.name)
#
#     def __del__(self):
#
#         print("%s 去了" % self.name)
#
# # tom 是一个全局变量
# tom = Cat("Tom")
# print(tom.name)
#
# # del 关键字可以删除一个对象
# del tom
#
# print("-" * 50)
# class Cat:
#     """这是一个猫类"""
#
#     def eat(self):
#         print("小猫爱吃鱼")
#
#     def drink(self):
#         print("小猫在喝水")
#
# tom = Cat()
# tom.drink()
# tom.eat()
# lazy_cat = Cat()
# lazy_cat.eat()
# lazy_cat.drink()
# class Cat:
#
#     def eat(self):
#         print("%s 爱吃鱼" % self.name)

# tom = Cat()
# tom.name = "Tom"
# tom.eat()
#
# lazy_cat = Cat()
# lazy_cat.name = "大懒猫"
# lazy_cat.eat()
# tom = Cat()
# tom.name = "Tom"
# tom.eat()
#
# print(tom)
class Cat:

    def __init__(self, name):

        self.name = name

        print("%s 来了" % self.name)

    def __del__(self):

        print("%s 去了" % self.name)

# tom 是一个全局变量
tom = Cat("Tom")
print(tom)

# del 关键字可以删除一个对象
del tom
print('-'*50)
# class Cat:
#
#     def __init__(self, new_name):
#
#         self.name = new_name
#
#         print("%s 来了" % self.name)
#
#     def __del__(self):
#
#         print("%s 去了" % self.name)
#
#     def __str__(self):
#         return "我是小猫：%s" % self.name
#
# tom = Cat("Tom")
# print(tom)
class Tool(object):

    # 使用赋值语句，定义类属性，记录创建工具对象的总数
    count = 0

    def __init__(self, name):
        self.name = name

        # 针对类属性做一个计数+1
        Tool.count += 1

    @classmethod
    def show_tool_count(cls):
        """显示工具对象的总数"""
        print("工具对象的总数 %d" % cls.count)

# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")


# 知道使用 Tool 类到底创建了多少个对象?
print("现在创建了 %d 个工具" % Tool.count)
Tool.show_tool_count()


class Game(object):
    # 游戏最高分，类属性
    top_score = 0

    @staticmethod
    def show_help():
        print("帮助信息：让僵尸走进房间")

    @classmethod
    def show_top_score(cls):
        print("游戏最高分是 %d" % cls.top_score)

    def __init__(self, player_name):
        self.player_name = player_name

    def start_game(self):
        print("[%s] 开始游戏..." % self.player_name)

        # 使用类名.修改历史最高分
        Game.top_score = 999


# 1. 查看游戏帮助
Game.show_help()

# 2. 查看游戏最高分
Game.show_top_score()


# 3. 创建游戏对象，开始游戏
game = Game("小明")


game.start_game()
# 4. 游戏结束，查看游戏最高分
Game.show_top_score()
def input_password():

    # 1. 提示用户输入密码
    pwd = input("请输入密码：")

    # 2. 判断密码长度，如果长度 >= 8，返回用户输入的密码
    if len(pwd) >= 8:
        return pwd

    # 3. 密码长度不够，需要抛出异常
    # 1> 创建异常对象 - 使用异常的错误信息字符串作为参数
    ex = Exception("密码长度不够")

    # 2> 抛出异常对象
    raise ex


try:
    user_pwd = input_password()
    print(user_pwd)
except Exception as result:
    print("发现错误：%s" % result)
a = input_password()
print(a)

