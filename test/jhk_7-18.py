# 用多进程和不用多进程下载文件
# from random import  randint
# from time import  time,sleep
#
#
# def download_task(filename):
#     print('开始下载%s....'% filename)
#     time_to_download = randint(5,10)
#     sleep(time_to_download)
#     print('%s下载完成！耗费了%d秒'% (filename,time_to_download))
#
#
# def main():
#     start = time()
#     download_task('python从入门到住院.pdf')
#     download_task('Peking Hot.avi')
#     end = time()
#     print('总共耗费了%.2f秒.' % (end - start))
#
#
# if __name__ == '__main__':
#     main()
# from multiprocessing import Process
# from os import getpid
# from random import randint
# from time import time,sleep
#
#
# def download_task(filename):
#     print('启动下载进程，进程号[%d].'% getpid())
#     print('开始下载%s....'% filename)
#     time_to_download = randint(5,10)
#     sleep(time_to_download)
#     print('%s下载完成！耗费了%d秒'%(filename,time_to_download))
#
#
# def main():
#     start = time()
#     p1 = Process(target = download_task,args = ('Python从入门到住院,pdf',))
#     p1.start()
#     p2 = Process(target= download_task, args= ('Peking Hot.avi',))
#     p2.start()
#     p1.join()
#     p2.join()
#     end = time()
#     print('总共耗费了%.2f秒'%(end - start))
#
#
# if __name__ == '__main__':
#     main()
# from multiprocessing import Process
# from time import sleep
#
# counter = 0
#
#
# def sub_task(string):
#     global counter
#     while counter <10:
#         print(string,end='',flush=True)
#         counter += 1
#         sleep(0.01)
#
#
# def main():
#     Process(target= sub_task,args=('Ping',)).start()
#     Process(target= sub_task,args= ('Pong',)).start()
#
#
# if __name__ == '__main__':
#     main()
# 多线程
# from random import randint
# from threading import Thread
# from time import time,sleep
#
#
# def download(filename):
#     print("开始下载%s....."%filename)
#     time_to_download = randint(3,7)
#     sleep(time_to_download)
#     print('%s下载完成！耗费了%d秒'%(filename,time_to_download))
#
#
# def main():
#     start = time()
#     t1 = Thread(target = download, args= ('Python从入门到住院.paf',))
#     t1.start()
#     t2 = Thread(target= download, args= ('Peking Hot.avi',))
#     t2.start()
#     t1.join()
#     t2.join()
#     end = time()
#     print('总共耗费了%.3f秒'%(end -start))
#
#
# if __name__ == '__main__':
#     main()
# "继承" 我们可以从已有的类创建新类
# 因此也可以通过继承Thread类的方式来创建自定义的线程类，然后再创建线程对象并启动线程
# from random import randint
# from threading import Thread
# from time import time,sleep
#
#
# class DownloadTask(Thread):
#
#     def __init__(self,filename):
#         super().__init__()
#         self._filename = filename
#
#     def run(self):
#         print("开始下载%s..."%self._filename)
#         time_to_download = randint(5,10)
#         sleep(time_to_download)
#         print('%s下载完成！耗费了%d秒'%(self._filename,time_to_download))
#
#
# def main():
#     start = time()
#     t1 = DownloadTask('Python从入门到住院',)
#     t1.start()
#     t2 = DownloadTask('Peking Hot.avi')
#     t2.start()
#     t1.join()
#     t2.join()
#     end = time()
#     print('总共耗费了%.02f秒'%(end - start))
#
#
# if __name__ == '__main__':
#     main()
# 100个线程向同一个银行账户转账的场景
# 银行账户就是一个灵界资源 在没有饱和的情况下我们很有可能会得到错误的结果
# from time import sleep
# from  threading import Thread
#
#
# class Account(object):
#
#     def __init__(self):
#         self._balance = 0
#
#     def deposit(self,money):
#         # 计算存款后的余额
#         new_balance = self._balance +money
#         # 模拟受理存款业务需要0.01秒的时间
#         sleep(0.01)
#         # 修改账户余额
#         self._balance = new_balance
#
#     @property
#     def blance(self):
#         return self._balance
#
#
# class AddMoneyThread(Thread):
#
#     def __init__(self,account,money):
#         super().__init__()
#         self._account = account
#         self._money = money
#
#     def run(self):
#         self._account.deposit(self._money)
#
# def main():
#     account = Account()
#     threads = []
#     # 创建100个存款的线程向同一个账户中存钱
#     for _ in range(100):
#         t = AddMoneyThread(account,1)
#         threads.append(t)
#         t.start()
#     # 等所有存款的线程都执行完毕
#     for t in threads:
#         t.join()
#     print('账户余额为：￥ %d元'% account._balance)
#
#
# if __name__ == '__main__':
#     main()
from time import sleep
from threading import Thread,Lock
'''
多个线程得到的账户余额都是初始状态下的0，所以都是0上面做了+1的操作，因此得到了错误的结果
在这种情况下，“锁”就可以派上用场了。我们可以通过“锁”来保护“临界资源”，只有获得“锁”的线程才能访问“临界资源”
而其他没有得到“锁”的线程只能被阻塞起来，直到获得“锁”的线程释放了“锁”，其他线程才有机会获得“锁”，进而访问被保护的“临界资源”。

'''
# from time import sleep
# from threading import Thread, Lock
#
#
# class Account(object):
#
#     def __init__(self):
#         self._balance = 0
#         self._lock = Lock()
#
#     def deposit(self, money):
#         # 先获取锁才能执行后续的代码
#         self._lock.acquire()
#         try:
#             new_balance = self._balance + money
#             sleep(0.01)
#             self._balance = new_balance
#         finally:
#             # 在finally中执行释放锁的操作保证正常异常锁都能释放
#             self._lock.release()
#
#     @property
#     def balance(self):
#         return self._balance
#
#
# class AddMoneyThread(Thread):
#
#     def __init__(self, account, money):
#         super().__init__()
#         self._account = account
#         self._money = money
#
#     def run(self):
#         self._account.deposit(self._money)
#
#
# def main():
#     account = Account()
#     threads = []
#     for _ in range(100):
#         t = AddMoneyThread(account, 1)
#         threads.append(t)
#         t.start()
#     for t in threads:
#         t.join()
#     print('账户余额为: ￥%d元' % account._balance)
#
#
# if __name__ == '__main__':
#     main()
# 将耗时的任务放到线程中以获得更好的用户体验
# import time
# import  tkinter
# import tkinter.messagebox
# #如果不使用“多线程”，我们会发现，当点击“下载”按钮后整个程序的其他部分都被这个耗时间的任务阻塞而无法执行了，这显然是非常糟糕的用户体验
#
#
# def download():
#     # 模拟下载任务需要花费10秒钟时间
#     time.sleep(10)
#     tkinter.messagebox.showinfo('提示','下载完成')
#
#
# def show_about():
#     tkinter.messagebox.showinfo('关于','作者：小白（version0.1）')
#
#
# def main():
#     top = tkinter.Tk()
#     top.title('单线程')
#     top.geometry('200x150')
#     top.wm_attributes('-topmost',True)
#
#     panel = tkinter.Frame(top)
#     button1 = tkinter.Button(panel, text='下载',command=download)
#     button1.pack(side='left')
#     button2 = tkinter.Button(panel,text = '关于',command=show_about)
#     button2.pack(side ='left')
#     panel.pack(side='bottom')
#
#     tkinter.mainloop()
#
#
# if __name__ == '__main__':
#     main()
# 使用多线程将耗时间的任务放到一个独立的线程中执行
# 这样就不会因为执行耗时间的任务而阻塞了主线程
# import time
# import tkinter
# import tkinter.messagebox
# from threading import Thread
#
#
# def main():
#     class DownloadTaskHandler(Thread):
#
#         def run(self):
#             time.sleep(10)
#             tkinter.messagebox.showinfo('提示','下载完成！')
#             # 启用下载按钮
#             button1.config(state = tkinter.NORMAL)
#
#     def download():
#         # 禁用下载按钮
#         button1.config(state=tkinter.DISABLED)
#         # 通过daemon参数将线程设置为守护线程（主程序退出后就不再保留执行）
#         # 在线程中处理耗时间的下载任务
#         DownloadTaskHandler(daemon=True).start()
#
#     def show_about():
#         tkinter.messagebox.showinfo('关于','作者:小白（v1.0）')
#
#     top = tkinter.Tk()
#     top.title('单线程')
#     top.geometry('200x500')
#     top.wm_attributes('-topmost', 1)
#
#     panel = tkinter.Frame(top)
#     button1 = tkinter.Button(panel, text='下载', command=download)
#     button1.pack(side='left')
#     button2 = tkinter.Button(panel, text='关于', command=download)
#     button2.pack(side='right')
#     panel.pack(side='bottom')
#
#     tkinter.mainloop()
#
# if __name__ == '__main__':
#     main()
# 使用多进程对复杂任务进行"分而治之"
# 完成1-100000000求和的计算密集任务
# 有问题 没找出 源码可以
# from time import time
#
#
# def main():
#     total = 0
#     number_list =[x for x in range(1,1000000001)] # 列表容器填入100000000个数，比较耗时间
#     start = time()
#     for number in number_list:
#         total += number
#     print(total)
#     end = time()
#     print('Execution time:%.3f'%(end -start))
#
#
# if __name__ =='__main__':
#     main()
# 将任务分解到8个进程中去执行
# #有问题 没找出 源码可以 写的一样的不行，上一个代码同样问题
# from multiprocessing import Process,Queue
# from random import randint
# from time import time
#
#
# def task_handle(curr_list, result_queue):
#     total = 0
#     for number in curr_list:
#         total += number
#         result_queue.put(total)
#
#
# def main():
#     processes = []
#     number_list = [x for x in range(1, 100000001)]
#     result_queue = Queue()
#     index = 0
#     # 启动8个进程将数据切片后进行运算
#     for _ in range(8):
#         p = Process(target=task_handle,
#                     args=(number_list[index:index + 12500000], result_queue))
#         index += 12500000
#         processes.append(p)
#         p.start()
#     # 开始记录所有进程执行完成花费时间
#     start = time()
#     for p in processes:
#         p.join()
#     # 合并执行结果
#     total = 0
#     while not result_queue.empty():
#         total += result_queue.get()
#     print(total)
#     end = time()
#     print('Execution time: ', (end - start), 's', sep='')
#
#
# if __name__ == '__main__':
#     main()
