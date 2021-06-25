import urllib.request
import re
title_number = 1
page_number = 1
url = "https://www.52pojie.cn/forum-24-1.html"  # 爬的地址

page = urllib.request.urlopen(url).read()  # 获取到该地址的所有内容
page = page.decode('gbk')  # 转码
# print(page)

# 正则表达式
zz1 = r'<tbody id="normalthread_.+?">(.+?)</tbody>'
# 匹配链接和标题
zz_link = r'<a href="(thread-.+?)".+? class="s xst">(.+?)</a>'

# 匹配所有符合规则的内容存到html集合里面
html = re.findall(zz1, page, re.S)  # re.S表示.可以代表\n
# print(html)
for line in html:
    html_link = re.findall(zz_link, line, re.S)  # re.S表示.可以代表\n
    # 标题
    title = html_link[0][1]
    # 链接
    link = html_link[0][0]
    print('%d\%s https://www.52pojie.cn/%s' % ( title_number,title, link))

 # 无敌分割线---------------------------------------
import urllib.request
import re

page_number = 1  # 页数
title_naumber = 1  # 每个帖子的编号
mData = {}
url = "https://www.52pojie.cn/forum-24-1.html"  # 爬第一页的地址
page = urllib.request.urlopen(url).read()  # 获取到该地址的所有内容
page = page.decode('gbk')  # 转码

zz_pageNumber = r'<span title="共.+?页">(.+?)</span>'
# 匹配出总页数
str_pagenumber = re.findall(zz_pageNumber, page, re.S)  # str_pagenumber = [' / 177 页', ' / 177 页']
# 将非数字用空字符串替换然后转化成int类型
page_Maxnumber = int(re.sub('\D', '', str_pagenumber[0]))  # \D表示非数字
# print(page_Maxnumber)
for index in range(page_Maxnumber):
    url = "https://www.52pojie.cn/forum-24-%d.html" % page_number  # 爬的地址
    if page_number > 2:
        page = urllib.request.urlopen(url).read()  # 获取到该地址的所有内容
        page = page.decode('gbk', 'ignore')  # 转码
    # 正则表达式
    # 匹配整个页面
    zz = r'<tbody id="normalthread_.+?">(.+?)</tbody>'
    # 匹配链接和标题
    zz_mData = r'<a href="(thread-.+?)".+? class="s xst">(.+?)</a>'

    # 匹配所有符合规则的内容存到html集合里面
    html = re.findall(zz, page, re.S)  # re.S表示.可以代表\n
    # print(html)
    for line in html:
        html_link = re.findall(zz_mData, line, re.S)  # 举例 ('thread-739688-1-1.html', '【Python】萌新跟我来入门Python爬虫')]
        # 标题
        title = html_link[0][1]  # '【Python】萌新跟我来入门Python爬虫'
        # 链接
        link = html_link[0][0]  # link = 'thread-739688-1-1.html'
        print('%d、%s https://www.52pojie.cn/%s' % (title_naumber, title, link))
        title_naumber = title_naumber + 1
    print("第%d页\n" % page_number)
    page_number = page_number + 1
# import requests
# import re
# import os
#
# # <img src="https://static.52pojie.cn/static/image/common/5yeas.gif" alt="五年荣誉奖章" style="margin-top: 20px;width:auto; height: auto;">
#
# url = "https://www.52pojie.cn/home.php?mod=medal"
#
# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}
#
# # 获取该地址的所有内容并转码
# page = requests.get(url, headers=header).content.decode('gbk', 'ignore')
#
# # 正则表达式
# pattern = re.compile('<img src="(https://static.52pojie.cn/static/image/common/.+?)" alt="(.+?)" style=".+?">', re.S)
#
# # 匹配所有符合规则的内容存到html集合里面
# html = pattern.findall(page)
#
#
# # print(html)
#
# # 写个方法创建文件夹
# def mkdir(path):
#     folder = os.path.exists(path)
#
#     if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
#         os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
#         print("创建新文件夹")
#
#         print("创建成功")
#     else:
#         print("该文件夹已经存在")
#
#
# # 调用方法,将文件夹路径传入
# img_path = "./照片/"
# mkdir(img_path)
#
# # 利用for循环来将集合里面的数据分离,然后判断链接是否是以gif为结尾,并存放图片
# i = 0
# for line in html:
#     line = html[i]
#     # 判断是否是gif图片
#     if str(line[0]).endswith("gif"):
#         p1 = line[0]
#         p2 = line[1]
#         print(p2 + " " + p1)
#         url = p1        # 下载gif图片放到D:/photo/文件夹里面
#         data = requests.get(url, headers=header).content
#         f = open(img_path + p2 + ".gif", "wb")
#         f.write(data)
#         f.close()
#     i = i + 1