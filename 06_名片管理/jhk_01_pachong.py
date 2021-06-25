# import requests
# #ozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0
# headers = {'User-Agent':'myagent'}
# url ='https://www.52pojie.cn/forum.php?mod=forumdisplay&fid=24&filter=typeid&typeid=29'
# r = requests.get(url,headers=headers)
# import urllib.request
# import re
# r = urllib.request.urlopen('https://www.52pojie.cn/forum-24-1.html')
# a  = r.read()# 提取页面源码
# a = a.decode("gbk")
# print(a)
import urllib.request
import re
import os

url = "https://www.52pojie.cn/home.php?mod=medal"  # 爬的地址
# <img src="https://static.52pojie.cn/static/image/common/5yeas.gif" alt="五年荣誉奖章" style="margin-top: 20px;width:auto; height: auto;">

page = urllib.request.urlopen(url).read()  # 获取到该地址的所有内容
page = page.decode('gbk')  # 转码
# print(page)

# 正则表达式
zz = r'<img src="([url=https://static.52pojie.cn/static/image/common/.+?]https://static.52pojie.cn/static/image/common/.+?[/url])" alt="(.+?)" style=".+?">'
# 匹配所有符合规则的内容存到html集合里面
html = re.findall(zz, page, re.S)  # re.S表示.可以代表\n
print(html)
i = 0

for line in html:
    line = html[i]
    # 判断是否是gif图片
    if str(line[0]).endswith("gif"):
        p1 = line[0]
        p2 = line[1]
        print(p2 + " " + p1)
    i = i + 1


def mkdir(path):
    folder = os.path.exists(path) # 用来检验给出的路径是否真地存在

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("创建新文件夹")

        print("创建成功")
    else:
        print("该文件夹已经存在")
img_path = "D:/photo/"
mkdir(img_path)
i = 0

for line in html:
    line = html[i]
    # 判断是否是gif图片
    if str(line[0]).endswith("gif"):
        p1 = line[0]
        p2 = line[1]
        print(p2 + " " + p1)
        url = p1
        # 下载gif图片放到D:/photo/文件夹里面
        web = urllib.request.urlopen(url)
        data = web.read()
        f = open(img_path + p2 + ".gif", "wb")
        f.write(data)
        f.close()
    i = i + 1