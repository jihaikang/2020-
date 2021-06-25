# '''
# 面试题：进程和线程的区别和联系
# 进程 — 操作系统分配内存的基本单位- 一个进程可以包含一个或多个线程
# 线程- 操作系统分配cpu的基本单位
# 并发编程(concurrent programming)
# 1. 提升执行性能 - 让程序中没有像因果关系的部分可以并发的执行
# 2. 改善用户体验- 让耗时间的操作不会造成程序的假死
# '''
#
# import glob
# import os
# import threading
#
# from PIL import Image
#
# PREFIX = 'thumbnails'
#
# def generrate_thumbnail(infile,size,format = 'PNG'):
#     '''生成指定图片文件的缩略图'''
#     file,ext = os.path.splitext(infile)
#     file = file[file.rfind('/' )+ 1:]
#     outfile = f'{PREFIX}/{file}_{size[0]}_{size[1]}.{exit}'
#     img = Image.open(infile)
#     img.thumbnail(size,Image.ANTIALIAS)
#     img.save(outfile,format)
#
# def main():
#     '''主函数'''
#     if not os.path.exists(PREFIX):
#         os.mkdir(PREFIX)
#     for infile in glob.glob('images/*.png'):
#         for size in (32,64,128):
#             # 创建并启动线程
#             threading.Thread(
#                 target=generrate_thumbnail,
#                 args=(infile,(size, size))
#             ).start()
#
#
# if __name__ == '__main__':
#     main()
# 多个线程竞争资源的情况。
"""
多线程程序如果没有竞争资源处理起来通常也比较简单
当多个线程竞争临界资源的时候如果缺乏必要的保护措施就会导致数据错乱
说明：临界资源就是被多个线程竞争的资源
"""
# import time
# import threading
#
# from concurrent.futures import ThreadPoolExecutor
#
#
# class Account(object):
#     '''银行账户'''
#
#     def __init__(self):
#         self.balance = 0.0
#         self.lock = threading.Lock()
#
#     def deposit(self,money):
#         # 通过锁保护临界资源
#         with self.lock:
#             new_balance = self.balance + money
#             time.sleep(0.001)
#             self.balance = new_balance
#
# class AddMoneyThread(threading.Thread):
#     '''自定义线程类'''
#
#     def __init__(self,account,money):
#         self.account = account
#         self.money = money
#         # 自定义线程的初始化方法中必须调用父类的初始化方法
#         super().__init__()
#
#         def run(self):
#             # 线程启动之后要执行的操作
#             self.account.deposit(self.money)
#
# def main():
#     '''主函数'''
#     account = Account()
#     # 创建线程池
#     pool = ThreadPoolExecutor(max_workers=10)
#     futures = []
#     for _ in range(100):
#     # 创建线程的第1种方式
#     # threading.Thread(
#     #     target=account.deposit, args=(1, )
#     # ).start()
#     # 创建线程的第2种方式
#     # AddMoneyThread(account, 1).start()
#     # 创建线程的第3种方式
#     # 调用线程池中的线程来执行特定的任务
#         future = pool.submit(account.deposit, 1)
#         futures.append(future)
#     # 关闭线程池
#     pool.shutdown()
#     for future in futures:
#         future.result()
#     print(account.balance)
#
# if __name__ == '__main__':
#     main()
"""
多个线程竞争一个资源 - 保护临界资源 - 锁（Lock/RLock）
多个线程竞争多个资源（线程数>资源数） - 信号量（Semaphore）
多个线程的调度 - 暂停线程执行/唤醒等待中的线程 - Condition
"""
# from concurrent.futures import ThreadPoolExecutor
# from random import randint
# from time import sleep
#
# import threading
#
#
# class Account():
#     """银行账户"""
#
#     def __init__(self, balance=0):
#         self.balance = balance
#         lock = threading.Lock()
#         self.condition = threading.Condition(lock)
#
#     def withdraw(self, money):
#         """取钱"""
#         with self.condition:
#             while money > self.balance:
#                 self.condition.wait()
#             new_balance = self.balance - money
#             sleep(0.001)
#             self.balance = new_balance
#
#     def deposit(self, money):
#         """存钱"""
#         with self.condition:
#             new_balance = self.balance + money
#             sleep(0.001)
#             self.balance = new_balance
#             self.condition.notify_all()
#
#
# def add_money(account):
#     while True:
#         money = randint(5, 10)
#         account.deposit(money)
#         print(threading.current_thread().name,
#               ':', money, '====>', account.balance)
#         sleep(0.5)
#
#
# def sub_money(account):
#     while True:
#         money = randint(10, 30)
#         account.withdraw(money)
#         print(threading.current_thread().name,
#               ':', money, '<====', account.balance)
#         sleep(1)
#
#
# def main():
#     account = Account()
#     with ThreadPoolExecutor(max_workers=10) as pool:
#         for _ in range(5):
#             pool.submit(add_money, account)
#             pool.submit(sub_money, account)
#
#
# if __name__ == '__main__':
#     main()
"""
多进程和进程池的使用
多线程因为GIL的存在不能够发挥CPU的多核特性
对于计算密集型任务应该考虑使用多进程
time python3 example22.py
real    0m11.512s
user    0m39.319s
sys     0m0.169s
使用多进程后实际执行时间为11.512秒，而用户时间39.319秒约为实际执行时间的4倍
这就证明我们的程序通过多进程使用了CPU的多核特性，而且这台计算机配置了4核的CPU
"""
# import concurrent.futures
# import math
#
# PRIMES = [
# 1116281,
#     1297337,
#     104395303,
#     472882027,
#     533000389,
#     817504243,
#     982451653,
#     112272535095293,
#     112582705942171,
#     112272535095293,
#     115280095190773,
#     115797848077099,
#     1099726899285419
# ] *5
#
# def is_prime(n):
#     '''判断素数'''
#     if n % 2 == 0:
#         return False
#
#     sqrt_n = int(math.floor(math.sqrt(n)))
#     for i in range(3,sqrt_n + 1, 2):
#         if n % i == 0:
#             return  False
#         return True
#
# def main():
#     '''主函数'''
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         for number,prime in zip(PRIMES,executor.map(is_prime,PRIMES)):
#             print('%d is prime：%s'% (number,prime))
#
# if __name__ == '__main__':
#     main()
'''
异步 I/O - async / await
'''
# import asyncio
#
#
# def num_generator(m,n):
#     '''指定范围的数字生成器'''
#     yield from range(m,n+1)
#
#
# async def  prime_filter(m,n):
#     '''素数过滤器'''
#     primes = []
#     for i in num_generator(m,n):
#         flag = True
#         for j in range(2,int(i ** 0.5 + 1)):
#             if i % j == 0:
#                 flag = False
#                 break
#         if flag:
#             print('Prime =>', i)
#             primes.append(i)
#
#         await asyncio.sleep(0.001)
#     return tuple(primes)
#
# async def square_mapper(m,n):
#     '''平方映射器'''
#     squares = []
#     for i in num_generator(m,n):
#         print('Square =>', i * i)
#         squares.append(i * i)
#
#         await  asyncio.sleep(0.001)
#     return squares
#
# def main():
#     '''主函数'''
#     loop = asyncio.get_event_loop()
#     future = asyncio.gather(prime_filter(2,100),square_mapper(1,100))
#     future.add_done_callback(lambda x: print(x.result()))
#     loop.run_until_complete(future)
#     loop.close()
#
#
# if __name__ == '__main__':
#     main()


#从5个URL中获取页面并通过正则表达式的
# 命名捕获组提取了网站的标题。
import asyncio
import re

import aiohttp

PATTERN = re.compile(r'\<title\>(?P<title>.*)\<\/title\>')

async def fetch_page(session, url):
    async with session.get(url,ssl=False) as resp:
        return await resp.text()


async def show_title(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch_page(session, url)
        print(PATTERN.search(html).group('title'))


def main():
    urls = ('https://www.python.org/',
            'https://git-scm.com/',
            'https://www.jd.com/',
            'https://www.taobao.com/',
            'https://www.douban.com/')
    loop = asyncio.get_event_loop()
    cos = [show_title(url) for url in urls]
    loop.run_until_complete(asyncio.wait(cos))
    loop.close()


if __name__ == '__main__':
    main()