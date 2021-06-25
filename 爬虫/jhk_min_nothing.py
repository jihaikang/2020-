# for num in range(100,1000):
#     low = num % 10
#     mid = num // 10 % 10
#     high = num // 100
#     if num == low ** 3 + mid ** 3 + high ** 3:
#         print(num)
# for x in range(0, 20):
#     for y in range(0, 33):
#         z = 100 - x - y
#         if 5 * x + 3 * y + z / 3 == 100:
#             print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))
import os
path = os.getenv('APPDATA')   #获取环境变量  pip换清华源
data = """[global]
timeout = 6000
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
trusted-host = pypi.tuna.tsinghua.edu.cn
"""
#  写入的数据
folder_path = os.path.join(path, "pip")
file_path = os.path.join(path, "pip", "pip.ini")
folder = os.path.exists(folder_path)  #判断文件夹是否存在
if not folder:
    os.mkdir(folder_path)  #创建文件夹
f = open(file_path, 'w')   #写文件
f.write(data)
f.close()
