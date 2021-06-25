"""
用户身份验证

version: 0.1
Author: jhk
"""
# uesname = input('请输入用户名：')
# password = input('请输入口令：')
# # 用户名是admin且密码是123456则身份验证成功否则身份验证失败
# if uesname == 'admin' and password == '123456':
#     print('身份验证成功！')
# else:
#     print('身份验证失败！')
'''
分段函数求值
        3x-5( x>1 )
f(x)=   x+2 ( -1<= x<= 1 )
        5x+3( x< -1 )
version:0.1
author:jhk
'''
# x = float(input('x= '))
# if x>1:
#     y = 3 * x - 5
# else:
#     if x >-1:
#         y = x+2
#     else:
#         y = 5 * x + 3
# print('f(%0.2f) = %0.2f'%(x,y))
'''
绘制单位英寸和公寸单位厘米互换
version:0.1
Author: jhk

'''
# value = float(input('请输入长度：'))
# unit = input('请输入单位：')
# if unit == 'in'or unit =='英寸':
#     print('%f英寸=%f厘米'%(value,value *2.54))
# elif unit == 'cm' or unit == '厘米':
#     print('%.2f厘米 = %.2f英寸' %(value,value /2.54))
# else:
#     print('请输入有效的单位')
'''
百分制成绩转换为登记制成绩
Version:0.1
Author:jhk

'''
# score = float(input('请输入成绩：'))
# if score >= 90:
#     grade = 'A'
# elif score >= 80:
#     grade = 'B'
# elif score >= 70:
#     grade = 'C'
# elif score >= 60:
#     grade ='D'
# else:
#     grade ='E'
# print('对应的等级是:', grade)
"""
判断输入的边长能否构成三角形，如果能则计算三角形的周长
和面积
Version:0.1
Author:jhk

"""
# a = float(input('a = '))
# b = float(input('b = '))
# c = float(input('c = '))
# if a + b > c  and a+c >b and b + c > a:
#     print('周长：%f'%(a+b+c))
#     p = (a+b+c)/2
#     area = (p *(p - a)*(p-b)* (p- c))**0.5
#     print('面积：%f' %(area))
# else:
#     print('无法构成三角形')
'''
用for 循环实现1-100求和

Version :
Author :

'''
# su = 0
# for x in range(101):
#     su+= x
# print(su)
'''
用for循环实现1—100之间的偶数求和
Version:\
Author:

'''
# a = 0
# for x in range(2,101,2):
#     # if x % 2 == 0:
#         a += x
# print(a)
'''
猜数字游戏
Version:
Author:

'''
# import random
# anwser = random.randint(1,100)
# counter = 0
# while True:
#     counter += 1
#     number = int(input('请输入：'))
#     if number < anwser:
#         print('大一点')
#     elif number >anwser:
#         print('小一点')
#     else:
#         print('恭喜你答对了！')
#         break
# print('你总共猜了%d'%(counter))
# if counter > 7:
#     print('你的智商余额显示不足！')
'''
九九乘法表
Version:
Author:
'''
# for i in range(1,10):
#     for j in range (1,i +1):
#         print('%d*%d=%d'%(i,j,i*j),end='\t')
#     print('')
'''
输入一个正整数判断它是不是素数
Version:
Author:
Date:2020-7-11
不知道cmath中的sqrt用法
'''
# import cmath
# num = int(input('请输入一个正整数：'))
# end = int(cmath.sqrt(num))
# is_prime = True
# for x in range(2,end+1):
#     if num % x == 0:
#         is_prime = False
#         break
# if is_prime and num  != 1:
#     print("%d是素数" %num)
# else:
#     print('%d不是素数'% (num))
'''
输入两个正整数
计算他们的最大公约数和最小公倍数
Version:
Author:
Date:
'''
# x = int(input('x = '))
# y = int(input('y = '))
# # 如果x大于y就i交换x和y的值
# if x > y:
#     x,y = y,x
# #从两个数中较大的数开始做递减的循环
# for factor in range(x,0,-1):
#     if x % factor == 0 and y % factor == 0:
#         print('%d和%d的最大公约数是%d'%(x,y,factor))
#         print('%d和%d的最小公倍数是%d'%(x,y,x*y //factor))
#         break
'''
打印三角形图案
Version:
Author:\
Date:
'''
row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()


for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()