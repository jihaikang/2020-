import os
a = "D:/pycharm/untitled"
print(os.listdir(a))
# action_str =input("请选择希望执行的操作：")
# print("您选择的操作是%s " % action_str)
# path ='./hppy'
# os.makedirs(path)
# print('创建成功')
# with open('fo.txt', 'w+') as f:#'w+'会清空，会创建 (文件已存在则清空，不存在则创建。)
#     f.write("2020/11/12")
#     f.seek(0)
#     date = f.read()
#     print(date)
#  删除文件
# f = os.rmdir("happpy")
os.remove("fo.txt")


