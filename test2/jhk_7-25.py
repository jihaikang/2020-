# 自定义字典限制只有在指定的key不存在时才能在字典中设置键值对
# class SetOnceMappingMixin():
#     '''自定义混入类'''
#     __slots__ = ()
#
#     def __setitem__(self, key, value):
#         if key in self:
#             raise KeyError(str(key) + 'already set')
#         return  super().__setitem__(key,value)
#
#
# class SetOnceDict(SetOnceMappingMixin,dict):
#     '''自定义字典'''
#     pass
#
#
# my_dict = SetOnceDict()
# try:
#     my_dict['username'] = 'xiaobai'
#     my_dict['username'] = 'hellokitty'
# except KeyError:
#     pass
# print(my_dict)
# 用元类实现单例模式。
# import threading
#
# class SingletonMeta(type):
#     '''自定义元类'''
#
#     def __init__(cls,*args,**kwargs):
#         cls.__instance = None
#         cls.__lock = threading.RLock()
#         super().__init__(*args,**kwargs)
#
#     def __call__(cls,*args,**kwargs):
#         if cls.__instance is None:
#             with cls.__lock:
#                 if cls.__instance is None:
#                     cls.__instance = super().__call__(*args,**kwargs)
#         return cls.__instance
#
# class President(metaclass=SingletonMeta):
#     '''总统类'''
#
#     pass
# 可插拔的哈希算法（策略模式）
# class StreamHasher:
#     '''哈希摘要生成器'''
#
#     def __init__(self,alg = 'md5',size=4096 ):
#         self.size = size
#         alg = alg.lower()
#         self.hasher = getattr(__import__('hashlib'), alg.lower())()
#
#     def __call__(self,stream):
#         return self.to_digest(stream)
#
#     def to_digest(self,stream):
#         '''生成十六进制形式的摘要'''
#         for buf in iter(lambda :stream.read(self.size),b''):
#             self.hasher.update(buf)
#         return self.hasher.hexdigest()
#
#
# def main():
#     '''主函数'''
#     hasher1 = StreamHasher()
#     with open('python3.6.7.txt','rb') as stream:
#         print(hasher1.to_digest(stream))
#     hasher2 = StreamHasher('sha1')
#     with open('python3.6.7.txt','rb')as stream:
#         print(hasher2(stream))
#
# if __name__ == '__main__':
#     main()
# 迭代器是实现了迭代器协议的对象
# class Fib(object):
#     '''迭代器'''
#
#     def __init__(self,num):
#         self.num = num
#         self.a , self.b = 0,1
#         self.idx = 0
#
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.idx < self.num:
#             self.a ,self.b = self.b,self.a + self.b
#             self.idx +=1
#             return self.a
#         raise  StopIteration
# 生成器是语法简化版的迭代器
# def fib(num):
#     '''生成器'''
#     a,b = 0, 1
#     for _ in range(num):
#         a, b = b, a + b
#         yield a
# 生成器进化为协程
# def calc_avg():
#     '''流式计算平均值'''
#     total, counter = 0, 0
#     avg_value = None
#     while True:
#         value = yield avg_value
#         total, counter = total + value,counter +1
#         avg_value = total / counter
#
# gen = calc_avg()
# next(gen)
# print(gen.send(10))
# print(gen.send(20))
# print(gen.send(30))
