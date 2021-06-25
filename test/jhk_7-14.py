list1 = [1,3,5,7,100]
print(list1) #[1,3,,5,7,100]
# 乘号表示列表元素的重复
list2 = ['hello'] *3
print(len(list1)) #计算列表长度（元素个数）
#下标（索引）运算
print(list1[0]) #1
print(list1[4]) # 100
# print(list[5]) # IndexError: list index out of range
print(list1[-1]) # 100
print(list1[-3]) #5
list1[2] = 300
print(list1) # [1,3,300,7,100]
# 通过循环用下标遍历列表元素
for index in range(len(list1)):
    print(list1[index])
# 通过for循环遍历列表元素
for elem in list1:
    print(elem)
#通过enumerate函数处理列表之后在遍历可以同时获得元素索引和值
for index,elem in enumerate(list1):
    print(index,elem)
list1 = [1,3,5,7,100]
# 添加元素
list1.append(200)
list1.insert(1,400)
# 合并两个列表
# lisr1.expend([1000,2000])
list1 += [1000,2000]
print(list1) # [1,400,3,5,7,100,200,1000,2000]
print(len(list1)) #9
# 先通过成员运算判断元素是否在列表中，如果存在就删除该元素
if 3 in list1:
    list1.remove(3)
if 1234 in list1:
    list1.remove(1234)
print(list1) # [1,400,5,7,100,200,1000,2000]
# 从指定的位置删除元素
list1.pop(0)
list1.pop(len(list1)-1)
print(list1)
# 清空列表元素
list1.clear()
print(list1)
fruits = ['grape','apple','strawberry','waxberry']
fruits += ['pitaya','pear','mango']
# 列表切片
fruits2 = fruits[1:4]
print(fruits2)
# 可以通过完整切片操作来复制列表
fruits3 = fruits[:]
print(fruits3)
fruits4 = fruits[-3:-1]
print(fruits4)
# 可以通过反向切片操作来获得倒转后列表的拷贝
fruits5 = fruits[::-1]
print(fruits5)
list1 = ['orange','apple','zoo','internationlization','blueberry']
list2 = sorted(list1)
# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 函数的设计就应该像sorted函数一样尽可能不产生副作用
list3 = sorted(list1,reverse=True)
#通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表排序
list4 = sorted(list1,key=len)
print(list1)
print(list2)
print(list3)
print(list4)
# 给列表发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)
print(list1)
f = [x for x in range(1,10)]
print(f)
f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)
# 用列表的生成表达式语法创建列表容器
# 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
f = [x ** 2 for x in range(1,1000)]
# print(sys.getsizeof(f)) # 查看对象占用内存的字节数
print(f)
# # 请注意下面的代码创建的不是一个列表二十一个生成器对象
# # 通过生成器可以获取到数据但它不占用额外的空间存储数据
# # 每次需要数据的时候就通过内部的运算得到数据（）需要花费额外的时间
# f = (x ** 2 for x in range(1,1000))
# # print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
# print(f)
# for val in f:
#     print(val)
# def fib(n):
#     a , b = 0 ,1
#     for _ in range(n):
#         a,b = b,a+b
#          yield a
# def main():
#     for va in fib(20):
#         print(va)
#
# if __name__  == '__main__':
#     main()
# 定义元组
# t = ('jhk',123,True,'江西')
# print(t)
# # 获取元组中的元素
# print(t[0])
# print(t[3])
# # 遍历元组中的值
# for member in t:
#     print(member)
# # 重新给元组赋值
# # t[0] = '123' # TypeError
#  # 变量t重新引用了新的元组原来的元组被垃圾回收
# t = ('王大锤')
# print(t)
# # 将元组转换成列表
# person = list(t)
# print(person)
# # 列表是可以修改他的元素
# person[0] = '李小龙'
# print(person)
# # 将列表转换成元组
# yuan_person = tuple(person)
# print(yuan_person)
# 创建集合的字面量语法
# set1 = {1,2,3,3,3,2}
# print(set1)
# print('length =',len(set1))
# # 创建集合的构造器语法
# set2 = set(range(1,10))
# set3 = set((1,2,3,3,2,1))
# print(set2,set3)
# # 创建集合的推导式语法
# set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
# print(set4)
# # 向集合添加元素和集合删除元素
# set1.add(4)
# set1.add(5)
# set2.update([11,12])
# set2.discard(5) #删除元素5
# if 4 in set2:
#     set2.remove(4)
# print(set1,set2)
# print(set3.pop())
# print(set3)
# # 集合的交集、并集、差集、对称差运算
# print(set1 & set2)
# #print(set1.intersection(set2))
# print(set1 | set2)
# # print(set1.union(set2))
# print(set1 - set2)
# # print(set1.difference(set2))
# print(set1^ set2)
# # print(set1.symmetric_difference(set2))
# # 判断子集和超集
# print(set2 <= set1)
# # print(set2.issubset(set1))
# print(set1 >= set2)
# # print(set1.issupersert(set2))
# print(set1 >= set3)
# # print(set.issuprest(set3))
# 创建字典的字面量语法
# scores = {'小白':95,'李元芳':78,'狄仁杰':82}
# print(scores)
# # 创建字典的构造器语法
# items1 = dict(one=1,two=2,three=3,foue=4)
# # 通过zip函数将两个序列压成字典
# items2 = dict(zip(['a','b','c'],'123'))
# # 创建字典的推导式语法
# items3 = {num: num ** 2 for num in range(1,10)}
# print(items1,items2,items3)
# # 通过键可以获取字典中对应的值
# print(scores['小白'])
# print(scores['狄仁杰'])
# # 对字典中所有键值对进行遍历
# for key in scores:
#     print(f'{key}：{scores[key]}')
# # 更新字典中的元素
# scores['李元芳'] = 65
# scores['诸葛亮'] = 71
# scores.update(冷面=67,方奇和=85)
# print(scores)
# if '武则天' in scores:
#     print(scores['武则天'])
# print(scores.get('武则天'))
# # get方法也是通过键获取对应的值但是可以设置默认值
# print(scores.get('武则天',60))
# # 删除字典中的元素
# print(scores.popitem())
# print(scores.popitem())
# print(scores.pop('小白',100))
# # 清空字典
# scores.clear()
# print(scores)
# 在屏幕上显示跑马灯文字
# import os
# import time
#
#
# def main():
#     content = '北京欢迎你为你开天辟地.....'
#     while True:
#         # 清理屏幕的输出
#         os.system('cls') # os.system('clear')
#         print(content)
#         # 休眠200毫秒
#         time.sleep(0.2)
#         content = content[1:] +content[0]
#     if __name__ =='__main__':
#         main()
# 设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成
# import random
# def generate_code(code_len =4):
#     '''
#     生成指定长度的验证码
#     :param code_len: 验证码的长度（默认4个字符）
#     :return: 有大小写字母和数字构成的随机验证码
#     '''
#     all_chars = '0123456789abcdefghijklmnopqrstuvwxyz'
#     last_pos = len(all_chars)-1
#     code = ''
#     for _ in range(code_len):
#         index = random.randint(0,last_pos)
#         code += all_chars[index]
#     return code
# print(generate_code())
# 设计一个函数返回给定文件名的后缀名
# def get_suffix(filename,has_dot =False):
#     '''
#     获取文件名的后缀名
#     :param filename: 文件名
#     :param has_dot: 返回的后缀是否需要带点
#     :return: 文件的后缀名
#     '''
#     pos = filename.rfind('.')
#     if 0<pos<len(filename)-1:
#         index = pos if has_dot else  pos +1
#         return filename[index:]
#     else:
#         return ''
# 设计一个函数返回传入的列表中最大和第二大的元素的值
# def max2(x):
#     m1,m2 = (x[0],x[1]) if x[0]>x[1] else (x[1],x[0])
#     for index in range(2,len(x)):
#         if x[index]>m1:
#             m2 =m1
#             m1 =x[index]
#         elif x[index]>m2:
#             m2 = x[index]
#     return  m1,m2
# print(max2([2,67,99]))
# 计算指定的年月日是这一年的第几天
# def is_leap_year(year):
#     '''
#     判断指定的年份是不是闰年
#     :param year: 年份
#     :return: 闰年返回True平年返回False
#     '''
#     return year % 4==0and year %100!= 0 or year%400==0
# def which_day(year,month,date):
#     '''
#     计算传入的日期是这一年的第几天
#     :param year: 年
#     :param mouth: 月
#     :param date: 日
#     :return: 第几天
#     '''
#     days_of_month = [
#         [31,28,31,30,31,30,31,31,30,31,30,31],
#         [31,29,31,30,31,30,31,31,30,31,30,31]][is_leap_year(year)]
#     total = 0
#     for index in range(month -1):
#         total +=days_of_month[index]
#     return total+date
#
# def main():
#     print(which_day(1980, 11, 28))
#     print(which_day(1981, 12, 31))
#     print(which_day(2014, 7, 2))
#     print(which_day(2020, 7, 14))
#
#
# if __name__ == '__main__':
#     main()
# 打印杨辉三角
# def main():
#     num = int(input('Number of rows: '))
#     yh =[[]] *num
#     for row in range(len(yh)):
#         yh[row] = [None] *(row+1)
#         for col in range(len(yh[row])):
#             if col == 0 or col ==row:
#                 yh[row][col] = 1
#             else:
#                 yh[row][col] =yh[row-1][col] + yh[row-1][col-1]
#             print(yh[row][col],end='\t')
#         print()
#
# if __name__ == '__main__':
#     main()
# from random import randrange,randint,sample
#
#
# def display(balls):
#     '''
#     输出列表中的双色球号码
#     '''
#     for index ,ball in enumerate(balls):
#         if index == len(balls) - 1:
#             print('|',end='')
#         print('%02d'%ball,end='')
#         print()
# def random_select():
#     '''
#     随机选择一组号码
#     :return:
#     '''
#     red_balls = [x for x in range(1,34)]
#     select_balls = []
#     select_balls = sample(red_balls,6)
#     select_balls.sort()
#     select_balls.append(randint(1,16))
#     return  select_balls
# def main():
#     n = int(input('机选几注：'))
#     for _ in range(n):
#         display(random_select())
#
#
# if __name__ == '__main__':
#     main()
# def main():
#     persons = [True] * 30
#     counter,index,number = 0,0,0
#     while counter <15:
#         if persons[index]:
#             number += 1
#             if number == 9:
#                 persons[index] = False
#                 counter += 1
#                 number = 0
#             index += 1
#             index %= 30
#         for person in persons:
#             print('基' if person else '非',end='')
#
# if __name__ == '__main__':
#     main()
# import  os
#
# def print_board(board):
#     print(board['TL']+'|'+board['TM']+'|'+board['TR'])
#     print('-+-+-')
#     print(board['ML']+'|'+board['MM']+'|'+board['MR'])
#     print('-+-+-')
#     print(board['BL']+'|'+board['BM']+'|'+board["BR"])
# def main():
#     init_board = {
#         'TL':'','TM':'','TR':'',
#         'ML':'','MM':'',"MR":'',
#         'BL':'','BM':'','BR':''
#     }
#     begin = True
#     while begin:
#         curr_board = init_board.copy()
#         begin = False
#         turn = 'x'
#         counter = 0
#         os.system('clear')
#         print_board(curr_board)
#         while counter <9:
#             move = input("轮到%s走棋，请输入位置："% turn)
#             if curr_board[move] =='':
#                 counter += 1
#                 curr_board[move] == turn
#                 if turn == 'x':
#                     turn = '0'
#                 else:
#                     turn ='x'
#             os.system('clear')
#             print_board(curr_board)
#         choice = input('再来一局？（yes|no）')
#         begin = choice ='yes'
#
#
# if __name__ == '__main__':
#     main()