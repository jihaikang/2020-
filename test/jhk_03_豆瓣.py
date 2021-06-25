# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# import requests
#
# """
# info:
# author:CriseLYJ
# github:https://github.com/CriseLYJ/
# update_time:2019-04-04
# """
#
# """
# 模拟登陆豆瓣
# """
#
#
# class DouBanLogin(object):
#     def __init__(self, account, password):
#         self.url = "https://accounts.douban.com/j/mobile/login/basic"
#         self.headers = {
#             "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
#         }
#         """初始化数据"""
#         self.data = {
#             "ck": "",
#             "name": account,
#             "password": password,
#             "remember": "true",
#             "ticket": ""
#         }
#         self.session = requests.Session()
#
#     def get_cookie(self):
#         """模拟登陆获取cookie"""
#         html = self.session.post(
#             url=self.url,
#             headers=self.headers,
#             data=self.data
#         ).json()
#         if html["status"] == "success":
#             print("恭喜你，登陆成功")
#
#     def get_user_data(self):
#         """获取用户数据表明登陆成功"""
#         # TODO: 这里填写你用户主页的url
#         url = "这里填写你用户主页的url"
#         # 获取用户信息页面
#         html = self.session.get(url).text
#         print(html)
#
#     def run(self):
#         """运行程序"""
#         self.get_cookie()
#         self.get_user_data()
#
#
# if __name__ == '__main__':
#     account = input("请输入你的账号:")
#     password = input("请输入你的密码:")
#     login = DouBanLogin(account, password)
#     login.run()
import requests
import re
import os
from hashlib import md5
from requests.exceptions import RequestException

"""
info:
author:CriseLYJ
github:https://github.com/CriseLYJ/
update_time:2019-3-6
"""

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'PHPSESSID=36c8n4lsbb8u63glevh1ksc9a1; webp_enabled=1; _ga=GA1.2.1167535880.1534758916; _gid=GA1.2.1330668796.1534758916; weilisessionid=aa3bf69b4f35c91ca4866315f1f300b1; wluuid=WLGEUST-02ADBA37-4B6C-DE33-2769-8697C4B575BB; wlsource=tc_pc_home; webp_enabled=0; _ga=GA1.3.1167535880.1534758916; _gid=GA1.3.1330668796.1534758916; _ba=BA0.2-20180820-51751-eyUyUL4rqUHUI1lh6uRM; qimo_seosource_e7dfc0b0-b3b6-11e7-b58e-df773034efe4=%E5%85%B6%E4%BB%96%E7%BD%91%E7%AB%99; qimo_seokeywords_e7dfc0b0-b3b6-11e7-b58e-df773034efe4=%E6%9C%AA%E7%9F%A5; accessId=e7dfc0b0-b3b6-11e7-b58e-df773034efe4; pageViewNum=1; bad_ide7dfc0b0-b3b6-11e7-b58e-df773034efe4=3c85f321-a45f-11e8-92ed-072415955da9; nice_ide7dfc0b0-b3b6-11e7-b58e-df773034efe4=3c85f322-a45f-11e8-92ed-072415955da9',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}


# 获取imageID
def get_imageID(term, page):
    try:
        print('获取图片ID.....')
        url = 'https://stock.tuchong.com/api/free/search/?term=' + term + '&page=' + str(page)
        req = requests.get(url, headers=headers)
        if req.status_code == 200:
            json_imageid = req.json()
            return parse_imgID(json_imageid)
    except ConnectionError:
        return None


# 解析imageID里面的图片id
def parse_imgID(imageID):
    print('解析imageID')
    data = imageID.get('data')
    hits = data.get('hits')
    if hits:
        print('存在ID,解析')
        for item in hits:
            Id = item.get('imageId')
            get_ImageJPG(Id)
        return True


# 拼接图片ID获取图片url
def get_ImageJPG(id):
    if id:
        try:
            print('拼接url访问网页')
            url = 'https://stock.tuchong.com/free/image/?imageId=' + str(id)
            req = requests.get(url, headers=headers)
            if req.status_code == 200:
                return parse_imgURL(req.text)
        except ConnectionError:
            return None


# 解析html里面的图片url
def parse_imgURL(html):
    if html:
        print('解析HTML图片URL...')
        url = re.findall('<div.*?class="image-cover".*?<img.*?src="(.*?)">.*?</div>', html, re.S)
        # url = re.findall('<title>(.*?)</title>', html, re.S)
        for item in url:
            print("准备下载...", item)
            download_image(item)
    return None


def download_image(url):
    try:
        urls = 'https:' + url
        ir = requests.get(urls, headers=headers)
        if ir.status_code == 200:
            save_image(ir.content)
        return None
    except RequestException:
        return None


def save_image(content):
    file_path = '{0}/{1}.{2}'.format(os.getcwd(), md5(content).hexdigest(), 'jpg')
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(content)
            f.close()
            print('下载成功----------------------')


def main():
    term = input('输入想要搜索的内容: ')
    for i in range(1, 7):
        get_imageID(term, i)


if __name__ == '__main__':
    main()