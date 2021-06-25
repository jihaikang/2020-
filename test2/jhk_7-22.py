# 生成式(推导式)的用法
# prices = {
#     'AAPL': 191.88,
#     'GOOG': 1186.96,
#     'IBM': 149.24,
#     'ORCl': 48.44,
#     'ACN': 166.89,
#     'FB': 208.09,
#     'SYMC': 21.29
# }
# # 用股票的价格大于100元的股票构造一个新的字典
# prices2 = {key: value for key, value in prices.items() if value >100}
# print(prices2)
# 嵌套列表的坑
# names = ['关羽','张飞','赵云', '马超', '黄忠']
# courses = ['语文','数学', '英语']
# # 录入五个学生三门课程的成绩
# # 错误 - 参考heep://pythontutor.com/visualize.html#mode=edit
# # scores = [[None]*len(courses)*len(names)]
# scores = [[None]* len(courses) for _ in range(len(names))]
# for row,name in enumerate(names):
#     for col, courses in enumerate(courses):
#         scores[row][col] = float(input(f'请输入{name}的{courses}成绩:'))
#         print(scores)
# heapq模块 (堆排序)
'''
从列表中找出最大的或最小的N个元素
堆结构(大根堆/小根堆)
'''
# import heapq
#
# list1 = [34,25,12,99, 87, 63, 58, 78, 88, 92]
# list2 = [
#     {'name':'IBM','shares':100, 'price': 91.1},
#     {'name':'AAPL','shares':50, 'price':543.22},
#     {'name':'FB', 'shares': 200, 'price': 21.09},
#     {'name':'HPQ', 'shares': 35, 'price':31.75},
#     {'name': 'YHOO', 'shares': 45, 'price':16.35},
#     {'name':'ACME', 'shares':75,'price':115.65}
#
# ]
# print(heapq.nlargest(3,list1))
# print(heapq.nsmallest(3,list1))
# print(heapq.nlargest(2,list2,key=lambda x: x['price']))# 排序前2位（大的）条件以x
# print(heapq.nlargest(2,list2,key=lambda x: x['shares']))
# itertools模块
'''
迭代工具模块
'''
# import itertools
#
# # 产生ABCD的全排列
# print(itertools.permutations('ABCD'))
# # 产生ABCDE的五选三组合
# print(itertools.combinations('ABCDE',3))
# # 产生ABCD和123的笛卡尔积
# itertools.product('ABCD','123')
# # 产生ABC的无线循环序列
# itertools.cycle(('A','B','C'))
# collections模块
'''
找出序列中出现次数最多的元素
'''
# from collections import Counter
#
# words = [
#     'look','into','my','eyes','look','into','my','eyes',
#     'the', 'eyes','the', 'eyes', 'the','eyes','not','around',
#     'the','eyes', "don't",'look','around','the','eyes',
#     'look', 'into','my','eyes',"you're",'under'
# ]
# counter = Counter(words)
# print(counter.most_common(3))
# 排序算法（选择、冒泡和归并）和查找算法(顺序和折半)
# def select_sort(items,comp=lambda x,y:x<y):
#     '''简单选择排序'''
#     items = items[:]
#     for i in range(len(items)-1):
#         min_index = i
#         for j in range(i+1,len(items)):
#             if comp(items[j],items[min_index]):
#                 min_index = j
#         items[i],items[min_index] = items[min_index],items[i]
#         return items
# def dubble_sort(items,comp=lambda x,y:x>y):
#     '''冒泡排序'''
#     items= items[:]
#     for i in range(len(items)-1):
#         swapped = False
#         for j in range(i,len(items)-1-i):
#             if comp(items[j],items[j+1]):
#                 items[j],items[j+1] = items[j+1],items[j]
#                 swapped = True
#         if not swapped:
#             break
#     return items
# def bubble_sort(items,comp=lambda x,y:x>y):
#     '''搅拌排序（冒泡排序升级版）'''
#     items = items[:]
#     for i in range(len(items)-1):
#         swapped = False
#         for j in range(i,len(items)-1-i):
#             if comp(items[j],items[j+1]):
#                 items[j],items[j+1] = items[j+1],items[j]
#                 swapped = True
#             if swapped:
#                 swapped = False
#                 for j in range(len(items)-2-i,i,-1):
#                     if comp(items[j-1],items[j]):
#                         items[j],items[j-1]=items[j-1],items[j]
#                         swapped = True
#
#                 if not swapped:
#                     break
#             return items
#
# def merge(items1,items2,comp=lambda x,y:x<y):
#     '''合并(将两个有序的列表合并成一个有序的列表)'''
#     items= []
#     index1,index2 = 0,0
#     while index1 < len(items1)and index2<len(items2):
#         if comp(items1[index1],items2[index2]):
#             items.append(items1[index1])
#             index1 += 1
#         else:
#             items.append(items2[index2])
#             index2 +=1
#     items += items1[index1]
#     items +=items2[index2]
#     return items
#
# def merge_sort(items,comp = lambda x,y:x<y):
#     return _merge_sort(list(items),comp)
#
# def _merge_sort(items,comp):
#     '''归并排序'''
#     if len(items) <2:
#         return items
#     mid = len(items)//2
#     left = _merge_sort(items[:mid],comp)
#     right = _merge_sort(items[:mid],comp)
#     return merge(left,right,comp)
# def seq_search(items,key):
#     '''顺序查找'''
#     for index,item in enumerate(items):
#         if item == key:
#             return index
#
#     return -1
# def bin_search(items,key):
#     '''折半查找'''
#     start, end = 0, len(items)-1
#     while start <= end:
#         mid = (start + end)//2
#         if key > items[mid]:
#             start = mid +1
#         elif key < items[mid]:
#             end = mid - 1
#         else:
#             return mid
#     return -1
# 穷举法
# 公鸡5元1只 母鸡3元1只 小鸡1元3只
# 用100元买100只鸡 问公鸡/母鸡/小鸡各多少只
# for x in range(20):
#     for y in range(33):
#         z = 100 - x - y
#         if 5 * x + 3 *y +z // 3 == 100 and z % 3 ==0:
#             print(x, y, z)
#
#
# # A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
# # 第二天A第一个醒来 他将🐟分为5分 扔掉多余的1条 拿走自己的一份
# # B第二个醒来 也将🐟分为5分 扔掉多余的1条 拿走自己的一份
# # 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼
# fish = 6
# while True:
#     total = fish
#     enough = True
#     for _ in range(5):
#         if (total -1)%5 == 0:
#             total = (total -1)//5*4
#         else:
#             enough = False
#             break
#     if enough:
#         print(fish)
#         break
#     fish +=5
'''
贪婪发：在对问题求解时，总是做出在当前看来是最好的选择，不追求最优解，快速找到满意解
输入：
20 6
电脑 200 20
收音机 20 4
钟 175 10
花瓶 50 2
书 10 1
油画 90 9
'''
# class Thing(object):
#     '''物品'''
#
#     def __init__(self,name,price,weight):
#         self.name = name
#         self.price = price
#         self.weight = weight
#
#     @property
#     def value(self):
#         '''价格重量比'''
#         return self.price / self.weight
#
# def input_thing():
#     '''输入物品信息'''
#     name_str,price_str,weight_str = input('请输入物品信息:').split()# 输入也会跟着遍历
#     return name_str,int(price_str),int(weight_str)
#
# def main():
#     '''主函数'''
#     max_weight,num_of_thing = map(int,input('请输入物品信息:').split())# 输入也会跟着遍历
#     all_things = []
#     for _ in range(num_of_thing):
#         all_things.append(Thing(*input_thing()))
#     all_things.sort(key=lambda x:x.value,reverse=True)
#     total_weight = 0
#     total_price = 0
#     for thing in all_things:
#         if total_weight + thing.weight <= max_weight:
#             print(f'小偷拿走了{thing.name}')
#             total_weight += thing.weight
#             total_price += thing.price
#     print(f'总价值:{total_price}美元')
#
#
# if __name__ == '__main__':
#     main()
# 分治法例子 ：快速排序
'''
快速排序 - 选择枢轴对元素进行划分，左边都比枢轴小右边都比枢轴大
'''
# def quick_sort(items,comp = lambda x,y:x <= y):
#     items = list(items)[:]
#     _quick_sort(items,0,len(items)-1,comp)
#     return  items
#
# def _quick_sort(items,start,end,comp):
#     if start < end:
#         pos = _partion(items,start,end,comp)
#         _quick_sort(items,start,pos-1,comp)
#         _quick_sort(items,pos +1,end,comp)
#
# def _partion(items,start,end,comp):
#     pivot = items[end]
#     i = start -1
#     for j in range(start,end):
#         if comp(items[j],pivot):
#             i += 1
#             items[i],items[j] = items[j],items[i]
#
#         items[i+1],items[end] = items[end],items[i+1]
#     return  i+1
# 回溯法例子：骑士巡逻
'''
递归回溯法：叫称为试探法，按选优条件向前搜索，当搜索到某一步，发现原先选择并不优或达不到目标时，
就退回一步重新选择，比较经典的问题包括骑士巡逻、八皇后和迷宫寻路等。
'''
# import sys
# import time
#
# SIZE = 5
# total = 0
#
# def print_board(board):
#     for row in board:
#         for col in row:
#             print(str(col).center(4),end='')
#             print()
#
# def patrol(board,row,col,step =1):
#     if row >= 0 and row < SIZE and \
#         col >= 0 and col <SIZE and \
#         board[row][col]==0:
#         board[row][col] = step
#         if step ==SIZE * SIZE:
#             global total
#             total +=1
#             print(f'第{total}种走法：')
#             print_board(board)
#         patrol(board, row - 2, col - 1, step + 1)
#         patrol(board, row - 1, col - 2, step + 1)
#         patrol(board, row + 1, col - 2, step + 1)
#         patrol(board, row + 2, col - 1, step + 1)
#         patrol(board, row + 2, col + 1, step + 1)
#         patrol(board, row + 1, col + 2, step + 1)
#         patrol(board, row - 1, col + 2, step + 1)
#         patrol(board, row - 2, col + 1, step + 1)
#         board[row][col] = 0
# def main():
#     board = [[0] * SIZE for _ in range(SIZE)]
#     patrol(board, SIZE - 1, SIZE - 1)
#
#
# if __name__ == '__main__':
#     main()
# 动态规划例子：子列表元素之和的最大值。
def main():
    items = list(map(int, input().split()))
    overall = partial = items[0]
    for i in range(1, len(items)):
        partial = max(items[i], partial + items[i])
        overall = max(partial, overall)
    print(overall)


if __name__ == '__main__':
    main()