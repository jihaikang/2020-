# for i in range(1,10):
#    for j in range(1,i+1):
#         print("%d*%d=%d"%(i,j,i*j),end="\t")
#    print("**")
# for i in range(1, 10):
#     for j in range(i, i + 1):
#        print('%d*%d=%d' % (i, j, i * j), end='\t')
#     print()
# for i in range(1,10):# 太注重格式了，缩进4字符
#     for j in range(1,i+1):
#         print("%d*%d=%d" % (i, j, i * j), end="\t")
# #     print()
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%d*%d=%d' % (i, j, i * j), end='\t')
#     print("***********************")
# for i in range(1,10):
#     for j in range(1, i+1):
#         print('%d * %d = %d'% (i, j ,i*j),end='\t')
#     print('**')
# for num in range(100, 1000):
#     low = num % 10
#     mid = num // 10 % 10
#     high = num // 100
#     if num == low ** 3 + mid ** 3 + high ** 3:
#         print(num)
# num = int(input('num = '))
# reversed_num = 0
# while num > 0:
#     reversed_num = reversed_num * 10 + num % 10
#     num //= 10
# print(reversed_num)
# for x in range(0, 20):
#     for y in range(0, 33):
#         z = 100 - x - y
#         if 5 * x + 3 * y + z / 3 == 100:
#             print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))
# from random import randint
# """
# CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
# 该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
# 简单的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；
# 其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；
# 其他点数，玩家继续要骰子，直到分出胜负。
# """
# # 个人建议 重点研究
# money = 1000
# while money > 0:
#     print('你的总资产为:', money)
#     needs_go_on = False
#     while True:
#         debt = int(input('请下注: '))
#         if 0 < debt <= money:
#             break
#     first = randint(1, 6) + randint(1, 6)
#     print('玩家摇出了%d点' % first)
#     if first == 7 or first == 11:
#         print('玩家胜!')
#         money += debt
#     elif first == 2 or first == 3 or first == 12:
#         print('庄家胜!')
#         money -= debt
#     else:
#         needs_go_on = True  #玩家第二次开始的条件
#     while needs_go_on:
#         needs_go_on = False
#         current = randint(1, 6) + randint(1, 6)
#         print('玩家摇出了%d点' % current)
#         if current == 7:
#             print('庄家胜')
#             money -= debt
#         elif current == first:
#             print('玩家胜')
#             money += debt
#         else:
#             needs_go_on = True
# print('你破产了, 游戏结束!')
# from random import randint#使用randint需要加上这句
# while True:
#     answer=randint(1,100)
#     if answer>70:
#         print(answer)
#     if answer<10:
#         print(answer)
#     if answer==20:
#         break
# a = 0
# 输出斐波那契数列的前20个数1 1 2 3 5 8 13 21 ...
# b = 1
# c= 0
# while c < 20:
#     a, b = b, a + b # 这也许就是python的魅力吧
#     print(a, end=' ')
#     c += 1
#     print(b,end=" ")
# num = int(input('请输入一个正整数: '))判断输入的正整数是不是回文数
# 回文数是指将一个正整数从左往右排列和从右往左排列值一样的数
# temp = num
# num2 = 0
# while temp > 0:
#     num2 *= 10
#     num2 += temp % 10
#     temp //= 10
# if num == num2:
#     print('%d是回文数' % num)
# else:
#     print('%d不是回文数' % num)
"""
找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数本身的数
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14
"""
# import math
# for num in range(1, 10000):#思路：就是找出完美数，那个num就是完美数,接着怎么找呢，
#     result = 0
#     for factor in range(1, int(math.sqrt(num)) + 1):
#         if num % factor == 0:
#             result += factor
#             if factor > 1 and num // factor != factor:
#                 result += num // factor
#     if result == num:
#         print(num)
import math
"""
输出2~99之间的素数

"""
# for num in range(2, 100):# 对数字的运用理解么，又是2个for
#     is_prime = True
#     for factor in range(2, int(math.sqrt(num)) + 1):
#         if num % factor == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num, end=' ')
# from random import randint
#
#
# def roll_dice(n=2):
#     """摇色子"""
#     total = 0
#     for _ in range(n):
#         total += randint(1, 6)
#     return total
#
#
# def add(a=0, b=0, c=0):
#     """三个数相加"""
#     return a + b + c
#
#
# # 如果没有指定参数那么使用默认值摇两颗色子
# print(roll_dice())
# # 摇三颗色子
# print(roll_dice(3))
# print(add())
# print(add(1))
# print(add(1, 2))
# print(add(1, 2, 3))
# # 传递参数时可以不按照设定的顺序进行传递
# print(add(c=50, a=100, b=200))

#
# def foo():
#     pass
#
#
# def bar():
#     pass
#
#
# # __name__是Python中一个隐含的变量它代表了模块的名字
# # 只有被Python解释器直接执行的模块的名字才是__main__
# if __name__ == '__main__':
#     print('call foo()')
#     foo()
#     print('call bar()')
#     bar()
#
#
# # 导入module3时 不会执行模块中if条件成立时的代码 因为模块的名字是module3而不是__main__
# def gcd(x, y):
#     """求最大公约数"""
#     (x, y) = (y, x) if x > y else (x, y) # 无论怎么样x都最大
#     for factor in range(x, 0, -1):
#         if x % factor == 0 and y % factor == 0:
#             return factor
#
#
# def lcm(x, y):
#     """求最小公倍数"""
#     return x * y // gcd(x, y)
# gcd(64,4)
# lcm(64,4)
# def is_palindrome(num):
#     """判断一个数是不是回文数"""
#     temp = num
#     total = 0
#     while temp > 0:
#         total = total * 10 + temp % 10
#         temp //= 10
#     if total == num:
#         print("输入回文数正确，您输入的会文是%d"%num)
#     else:
#         print("输入错误")
#     return total == num
# is_palindrome(111)