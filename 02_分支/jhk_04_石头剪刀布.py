# # 导入工具包
# import random
# # 输入
# player = int(input("请输入你想要出的拳 拳头1 剪刀2 布3 ："))
# compete = random.randint(1, 3)
# print("玩家选择的拳头是%d - 电脑选择的拳头是%d" % (player, compete))
# if ((player == 1 and compete == 2)
#         or (player == 2 and compete == 3)
#         or(player == 3 and compete == 1)):
#     print("欧耶，电脑弱爆了")
# elif player == compete:
#     print("我们真是心有灵犀啊，再来")
# else:
#     print("我们决战到天亮")
# str='aeiou'
# def pig(s):
#     n=len(s)
#     i=0
#     for j in range(5):
#        if s[i] == str[j]:# 循环遍历出s[i]为辅音字母时的值
#           i+=1
# #下面的是分情况输出值
#     if i==n-1:#辅音字母最后时
#        return s+'-ay'
#     else:
#        return s[0:i]+s[i+1:]+'-'+s[i]+'ay'# 辅音字母不是最后一个时
# print(pig('aeery'))
#
# def Quzh_Statistics_Vowel(strString):
#     """
#     统计元音字母——输入一个字符串，统计处其中元音字母的数量。
#     更复杂点的话统计出每个元音字母的数量。
#     """
#     # 元音字母总个数
#     num = 0
#     # 每个元音字母的数量
#     num_a = 0
#     num_e = 0
#     num_i = 0
#     num_o = 0
#     num_u = 0
#     for t in strString:
#         # 避免忽视大写字母
#         i = t.lower()
#         # 统计出元音字母的总数量
#         if i in ['a', 'e', 'i', 'o', 'u']:
#             num += 1
#         # 统计出每个元音字母的数量
#         if i == 'a':
#             num_a += 1
#         elif i == 'e':
#             num_e += 1
#         elif i == 'i':
#             num_i += 1
#         elif i == 'o':
#             num_o += 1
#         elif i == 'u':
#             num_u += 1
#     print("元音字母总个数是:%s" % num)
#     print("其中a有%s个,e有%s个,i有%s个,o有%s个,u有%s个" % \
#     (str(num_a), str(num_e), str(num_i), str(num_o), str(num_u)))
#
#
# Quzh_Statistics_Vowel('This is A good man Hello world you are my boby')
# def judge(string):#判断是否为回文——判断用户输入的字符串是否为回文。回文是指正反拼写形式都是一样的词，譬如“racecar”。
#     mylength = len(string)
#     if mylength < 2:
#         return True
#     else:
#         for i in range(int((mylength + 1) / 2)):# 找中间那个数
#             if obj[i] == obj[mylength - 1 - i]: #前后序列相等，以找出的中间数为界限
#                 i += 1
#             else:
#                 return False
#             return True
#
# obj = [1, 2, 3, 2, 2]
# print(judge(obj))
# print(obj == obj[::-1])# 原来输出2变量相等，输出的是Ture，大家都是Ture的话那不是可以统计了
# from collections import Counter
# import re
# """统计字符串中单词的数目"""
# cnt = Counter()
#
# f = open("mytest.txt","rb")
# for a in f:
#     print(a)
#     a = a.lower()
#     # 正则表达式替换特殊字符
#     # w = w.replace("\n","");
#     a = re.sub("[！,\n,!]", "", a)
#     for word in a.split(" "):
#         cnt[word] += 1
#
# print(cnt)

#可以包装成可以计算包含多少个单词的函数
def count_words(filename):
    """计算一个文件大约有多少个单词"""
    try:
        with open(filename,encoding='utf-8')as f_obj:
            contents=f_obj.read()
    except FileNotFoundError as e:
        msg=" sorry "+filename +"not exist"
        print(msg)
    else:
        words=contents.split()# split()可以以空格为分隔符，把字符串拆分，储存在列表中
        num_words=len(words)
        print("The file "+filename +"has about "+str(num_words)+" words")


filename='alice.txt'
count_words(filename)