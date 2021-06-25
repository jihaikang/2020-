# def a():
#     print('A')
#     return 1
#
#
# def b():
#     print('B')
#     return 1
#
#
# def c():
#     print('C')
#     return []
#
#
# def d():
#     print('D')
#     return 1
#
#
# def e():
#     print('E')
#     return []
#
#
# if a() or b() or c() or d() or e():
#     print('ok')
# _metaclass_ = type
# class A:
#     def hello(self):
#         print('hello . I am A.')
# class B(A):
#     pass
# a = A()
# b = B()
# b.hello()
# a.hello()
# import datetime
# now = datetime.datetime.now().date()
# print(now)
# import copy
#
# will = ['Will',28,['python','c#','JavaScript']]
# wilber = copy.copy(will)
# print(id(will))
# print(will)
# print([id(ele)for ele in will ])
# print(id(wilber))
# print(wilber)
# print([id(ele) for ele in wilber])
# will[0] = 'Wilber'
# will[2].append('CSS')
# print(id(will))
# print(will)
# print([id(ele)for ele in will])
# print(id(wilber))
# print(wilber)
# print([id(ele)for ele in wilber])
# def foo(bar=None):
#     if bar is None:
#         bar = []
#     bar.append('baz')
#
#     return bar
#
# foo()
# try:
#     l = ['a','b']
#     int(l[2])
# except(ValueError,IndexError) as e:
#     pass
# class A():
#     pass
# print(dir(A))
# class another(object):
#     def __init__(self, *args, **kwargs):
#         print("init")
#     def __new__(cls,*args,**kwargs):
#         print("newano")
#         return object.__new__(cls, *args, **kwargs)
# class display(object):
#     def __init__(self, *args, **kwargs):
#         print("init")
#     def __new__(cls, *args, **kwargs):
#         print("newdis")
#         print(type(cls))
#         return another.__new__(cls, *args, **kwargs)
# a=display()
# __author__ = 'pythontab.com'
# #导入pymysql的包
# import pymysql
# try:
#     #获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
#     conn=pymysql.connect(host='localhost',user='pythontab',passwd='pythontab',db='pythontab',port=3306,charset='utf8')
#     cur=conn.cursor()#获取一个游标
#     cur.execute('select * from user')
#     data=cur.fetchall()
#     for d in data :
#         #注意int类型需要使用str函数转义
#         print("ID: "+str(d[0])+'  用户名： '+d[1]+"  注册时间： "+d[2])
#     cur.close()#关闭游标
#     conn.close()#释放数据库资源
# except  Exception :print("查询失败")
# import sys
# import pprint
# pprint.pprint(sys.path)
# from threading import Thread
# import subprocess
# from queue import Queue
# num_threads = 3
# ips = ['10.108.100.174','119.75.218.77','127.0.0.1']
# q = Queue()
# def pingit(i,queue):
#     while True:
#         ip = queue.get()
#         print('thread %s is pinging %s'% (i,ip))
#         ret = subprocess.call('ping -c 3 %s'%ip,shell=True,stdout=open('.python3.6.7.txt','w'))
#         if ret != 0:
#             print('%s is down'% ip)
#         queue.task_done()
#
# for i in range(num_threads):
#     t = Thread(target=pingit,args=(i, q))
#     t.setDaemon(True)
#     t.start()
# for ip in ips:
#     q.put(ip)
# print('main thread is waiting...')
# q.join()
# print('Done....')
# import Cookie
# import datetime
# import random
#
# expiration = datetime.datetime.now() +datetime.timedelta(days=30)
# cookie = Cookie.SimpleCookie()
# cookie['session'] = random.randint(1,1000000000)
# cookie['session']['domain'] = '.baidu.com'
# cookie['session']['path'] = '/'
# cookie['session']['expires'] = expiration.strftime('%a.%d-%b-%Y %H:%M:%S PST')
#
# print('Content-type: text/plain')
# print(cookie.output())
# print()
# print('Cookie set with:' + cookie.output)