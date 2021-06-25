# import requests
# import re
# import cv2
# from PIL import ImageFont, ImageDraw, Image
# import numpy
#
#
# # 定义一个晚安表情包函数wanan，主要就是在图片上加上“晚安”，这样显得我是在关心她，而不是斗图！
# def wanan(file_name):
#     bk_img = cv2.imread(file_name)  # 读取图片，默认是彩色
#     fontpath_wz = "Alibaba-PuHuiTi-Heavy.otf"  # 设置需要显示的字体为“阿里普惠字体”，用什么方正啊，一不小心就被告，阿里家的不嫖白不嫖
#     font_wz = ImageFont.truetype(fontpath_wz, 350)  # 创建字体对象，设置字体大小
#     img_pil = Image.fromarray(bk_img)  # 实现array到image的转换
#     draw = ImageDraw.Draw(img_pil)  # 创建对象
#     draw.text((500, 500), "晚安！", font=font_wz, fill=(255, 255, 255))  # 设置文字位置，内容，字体，颜色
#     bk_img = numpy.array(img_pil)  # 将信息写入
#     cv2.imshow("good night", bk_img)  # 展示显示图片
#     cv2.imwrite(file_name + "wanan.jpg", bk_img)  # 保存图片
#
#
# # 设置一个请求头来伪装，以突破美团的反爬
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/78.0.3809.100 Safari/537.36',
#     'Cookie': '_lxsdk_cuid=1705c1232e5c8-0b3dd2a7bd22a7-3b65410e-1fa400-1705c1232e560; _hc.v=f33fac6e-a350-7eb0-bb31-ac1e31f6293e.1583081446; Hm_lvt_f66b37722f586a240d4621318a5a6ebe=1583081431,1583163970; __utma=211559370.503033648.1583081432.1583081432.1583163971.2; __utmz=211559370.1583163971.2.2.utmcsr=baidu|utmccn=baidu|utmcmd=organic|utmcct=zt_search; ci=1; rvct=1%2C73; _lxsdk=1705c1232e5c8-0b3dd2a7bd22a7-3b65410e-1fa400-1705c1232e560; _lx_utm=utm_source%3Dbaidu%26utm_campaign%3Dbaidu%26utm_medium%3Dorganic%26utm_content%3Dzt_search; client-id=80b56a14-c077-4c81-97f8-c7e6ba86afce; lat=30.47633; lng=114.39492; _lxsdk_s=170c74d7fea-2d8-f79-b1%7C%7C30; uuid=0efec67097ed4dceba5e.1583896774.1.0.0; mtcdn=K; lt=8GRjAM7XkxZcWL24k3Eru8ZATtYAAAAAKgoAALH5-kQry4ohn4eehoxfWaRUoIonADbDqM5EIWtchvxfrTh56O0RajiylAPl1D1dQQ; u=2806660198; n=%E6%9D%8E%E6%99%93%E9%B9%8F614; token2=8GRjAM7XkxZcWL24k3Eru8ZATtYAAAAAKgoAALH5-kQry4ohn4eehoxfWaRUoIonADbDqM5EIWtchvxfrTh56O0RajiylAPl1D1dQQ'
# }
# for num in range(1, 10):  # 依次循环1-10,10页应该够了！不够的话，我再加！不就是改个数字嘛，so easy！
#     url = "https://wh.meituan.com/meishi/pn" + str(num) + "/"  # 构建拼接一下网址，用于访问
#     res = requests.get(url, headers=headers)  # 用requests.get（）函数访问页面，用headers=headers伪装
#     print(res.text)  # 打印看一下信息
#     shop_ids = re.findall('"poiId":(.*?),"frontImg":', res.text)  # 商家的页面都是id不同，所以就提取出来商家的id就可以了
#     print(shop_ids)  # 看一下商家的ids
#     for shop_id in shop_ids:  # 依次从商家ids中提取商家id，然后构造网址
#         for i in range(0, 100, 10):  # 评论的链接只有商家id和展示数字出现变化（0,10,20,30），因此就再用一个循环来生成（0,10,20……），就搞10页吧，不够了就改数字
#             try:
#                 # 构建拼接网址
#                 shop_url = "https://www.meituan.com/meishi/api/poi/getMerchantComment?uuid=0efec67097ed4dceba5e.1583896774.1.0.0&platform=1&partner=126&originUrl=https%3A%2F%2Fwww.meituan.com%2Fmeishi%2F" + str(
#                     shop_id) + "%2F&riskLevel=1&optimusCode=10&id=" + str(shop_id) + "&userId=2806660198&offset=" + str(
#                     i) + "&pageSize=10&sortType=1"
#                 res = requests.get(shop_url, headers=headers)  # 访问获得评论信息
#                 pj_json = res.json()  # 转换数据类型为json
#                 yhpjs = pj_json['data']['comments']  # 提取出来用户评论信息
#                 for yhpj in yhpjs:  # 依次循环获得用户评价
#                     pic_urls = yhpj['picUrls']  # 得到用户评价中的图片链接
#                     try:
#                         print(pic_urls[0]['url'])
#                         picurl = pic_urls[0]['url']  # 得到用户评价的图片网址
#                         res = requests.get(picurl, headers=headers, timeout=15)  # 访问图片网址，设定15秒超时
#                         file_name = picurl.split('/')[-1]  # 取每个picurl最后的部分
#                         with open(file_name, "wb") as f:  # 打开文件名为file_name的文件，相当于新建file_name文件
#                             f.write(res.content)  # 将获得的图片信息写入进去
#                             print("保存完毕！")  # 保存完成！
#                             wanan(file_name)  # 调用wanan（）函数来制作表情包
#                             print("晚安表情包制作完成！")  # 制作表情包完成
#                     except:  # 出错就pass，数据多，不怕失败！就是这么自信！
#                         pass
#             except:  # 出错就pass，数据多，不怕失败！就是这么自信！
#                 pass
#             a = ([1, 2, 3])
# import urllib.request
# import re
# import chardet
#
# def getHtml(url):
#     page= urllib.request.urlopen(url)
#     html= page.read()
#
#     page.close()
#     return html
#
# def getWeather(html):
#     reg = '<a title=.*?>(.*?)</a>.*?<span>(.*?)</span>.*?<b>(.*?)</b>'
#     weatherList= re.compile(reg).findall(html)
#     return weatherList
#
# url = 'http://www.weather.com.cn'
# html = getHtml(url)
# encode_type = chardet.detect(html)
# html = html.decode(encode_type['encoding'])
# list = getWeather(html)
# print(list)
# import requests
# from bs4 import BeautifulSoup
# from pymongo import MongoClient
#
#
# class QuNaEr():
#     def __init__(self, keyword, page=1):
#         self.keyword = keyword
#         self.page = page
#
#     def qne_spider(self):
#         url = 'https://piao.qunar.com/ticket/list.htm?keyword=%s&region=&from=mpl_search_suggest&page=%s' % (
#         self.keyword, self.page)
#         response = requests.get(url)
#         response.encoding = 'utf-8'
#         text = response.text
#         bs_obj = BeautifulSoup(text, 'html.parser')
#
#         arr = bs_obj.find('div', {'class': 'result_list'}).contents
#         for i in arr:
#             info = i.attrs
#             # 景区名称
#             name = info.get('data-sight-name')
#             # 地址
#             address = info.get('data-address')
#             # 近期售票数
#             count = info.get('data-sale-count')
#             # 经纬度
#             point = info.get('data-point')
#
#             # 起始价格
#             price = i.find('span', {'class': 'sight_item_price'})
#             price = price.find_all('em')
#             price = price[0].text
#
#             conn = MongoClient('localhost', port=27017)
#             db = conn.QuNaEr  # 库
#             table = db.qunaer_51  # 表
#
#             table.insert_one({
#                 'name': name,
#                 'address': address,
#                 'count': int(count),
#                 'point': point,
#                 'price': float(price),
#                 'city': self.keyword
#             })
#
#
# if __name__ == '__main__':
#     citys = ['北京', '上海', '成都', '三亚', '广州', '重庆', '深圳', '西安', '杭州', '厦门', '武汉', '大连', '苏州']
#     for i in citys:
#         for page in range(1, 5):
#             qne = QuNaEr(i, page=page)
#             qne.qne_spider()
# encound=utf-8
# import urllib.request
# from bs4 import BeautifulSoup
#
# res = urllib.request.urlopen("http://www.douban.com/tag/%E5%B0%8F%E8%AF%B4/?focus=boo")
# sope = beautifulsope.beautifulsope(res)
# boke_div = sope.find(attrs={"id:book"})
# book_a = sope.findall(attrs ={"class:title"})
# for book in book_a:
#     print(book.string)
# import ssl
# import os
# import urllib.request
# import requests
# from bs4 import BeautifulSoup
#
#
# ssl._create_default_https_context =ssl._create_unverified_context()
# headers = { 'User-Agent':
#         'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',}
# if not os.path.exists("./插画素材/"):
#     os.makedirs("./插画素材/")
# else:
#     print('报错')
#
# url = "https://www.tupianzj.com/meinv/mm/meizitu/"
# html = requests.get(url,headers=headers).text
# soup = BeautifulSoup(html,"lxml")
# images_data = soup.find('ul', class_='d1 ico3').find_all_next('li')
# for image in images_data:
#     image_url = image.find_all('img')
#     for _ in image_url:
#         print(_['src'],_['alt'])
#
# try:
#     urllib.request.urlparse(_['src'],'./插画素材/'+_['alt'] + ".jpg")
# except:
#     print('wrong')

import requests
from lxml import etree

# 怼人表情包网址http://www.doutula.com/search?type=photo&more=1&keyword=%E6%80%BC%E4%BA%BA&page=8
# 规律一眼就发现是改个数字就行了，就用for i inrange（）

for i in range(1, 2):  # 上次给女朋友发了20000句情话，你们说发的太多，所以这次就爬50页，也就50*72=3600个表情包，打败她应该够了，不够再爬
    url = "http://www.doutula.com/search?type=photo&more=1&keyword=%E6%80%BC%E4%BA%BA&page=" + str(i)  # 用数字拼接网址
    res = requests.get(url).text  # 用requests.get（）函数获得拼接网址的数据
    # print(res)    #打印显示一下
    res_xpath = etree.HTML(res)  # 转换为xpath可用的格式
    # 用xpath提取表情包的具体网址
    bqb_urls = res_xpath.xpath('//*[@id="search-result-page"]/div/div/div[2]/div/div[1]/div[1]/div//img/@data-original')
    for bqb_url in bqb_urls:  # 依次循环提取表情包网址
        try:
            res = requests.get(bqb_url).content  # 获得二进制数据
            file_name = bqb_url.split('/')[-1]  # 表情包名字就取网址中的最后一个
            with open("./file_name/", 'wb') as f:  # 用“wb”模式打开，没有就新建，肯定是需要自动新建的
                f.write(res)  # 将获得的二进制数据写到文件中
        except:
            pass  # 3600个，失败几个无所谓的，不在乎
print("表情包爬取完成，准备战斗吧！")