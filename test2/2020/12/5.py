import requests  # 第三方库解析浏览器
import lxml.html
etree = lxml.html.etree

url = 'https://www.huya.com/g/4079'  # 目标网址

response = requests.get(url=url)  # 解析获取源代码   这种时候纯文本 需要正则 太麻烦
#print(response.text)  # 打印 有时候是看不懂的转化UTF-8

data = etree.HTML(response.text)#数据解析  可以有缩少案件了
#print(data)
girls = data.xpath('//img[@class="pic"]')
print(girls)
#
# for girl in girls:
#     img_url = girl.xpath('./@data-original')[0]
    #print(img_url)  #缩小后的图片
#     img_url = img_url.split("?")[0]
    # print(img_url)  #原图
    # name = girl.xpath('./@alt')[0]  #定义名称
    #
    # image = requests.get(url=img_url)  #图片的数据
    # with open ('./%s.jpg' % name,'wb') as jpg:  #需要在python目录下创建Girl文件夹
    #     jpg.write(image.content)
    #     print('《%s》下载完成' % name)