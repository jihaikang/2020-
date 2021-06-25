# # # coding=utf-8
# #
# # import os, time, requests, re
# # from lxml import etree
# #
# # headers = {
# #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
# #     'Referer': 'https://www.meitulu.com/t/changtui/',
# #     'Cookie': 'UM_distinctid=16f94d6dc9e568-0898b8c4c5d86b-645d7c2d-144000-16f94d6dc9f2f2; CNZZDATA1255357127=738626102-1578744969-%7C1578747140'
# # }
# #
# # 'https://www.meitulu.com/gangtai/'
# # main_url = 'https://www.meitulu.com/t/changtui/'
# # resp = requests.get(main_url, headers=headers)
# # text = resp.content.decode('utf-8')
# # html = etree.HTML(text)
# #
# # print('输入数字并按回车确定：3=日韩美女（96页），4=港台美女（16页），5=国产美女（222页）：')
# # start = int(input('start:'))
# #
# # for li in html.xpath('//ul[@class="menu"]/li')[start:start + 1]:
# #     frnqu_url = li.xpath('.//@href')[0]
# #     frnqu_name = li.xpath('./a/text()')[0]
# #     print(frnqu_url, frnqu_name)
# #     resp = requests.get(frnqu_url, headers=headers)
# #     text = resp.content.decode('utf-8')
# #     html = etree.HTML(text)
# #     pages = 1
# #     try:
# #         pages = html.xpath('//*[@id="pages"]/a/text()')[-2]
# #     except:
# #         pages = 1
# #     start_page = int(input('输入开始页数 1-%s，回车确定:' % pages))
# #     end_page = int(input('输入结束页数 1-%s，回车确定:' % pages))
# #     for page in range(start_page, int(end_page) + 1):
# #         detil_url = frnqu_url + '%s.html' % page
# #         # if detil_url == 'https://www.meitulu.com/t/fengsuniang/1.html':detil_url = frnqu_url
# #         if page == 1: detil_url = frnqu_url
# #         print(detil_url)
# #         try:
# #             resp = requests.get(detil_url, headers=headers)
# #         except:
# #             time.sleep(5)
# #             resp = requests.get(detil_url, headers=headers)
# #         text = resp.content.decode('utf-8')
# #         html = etree.HTML(text)
# #         for li in html.xpath('//ul[@class="img"]/li'):
# #             title = li.xpath('string(.//p[@class="p_title"]/a/text())')
# #             title = re.sub('[\/:*?"<>|]', ' ', title)
# #             urls = li.xpath('./p[@class="p_title"]/a/@href')[0]
# #             if not re.findall('https', urls):
# #                 url = 'https://www.meitulu.com' + urls
# #             else:
# #                 url = urls
# #             img = [li.xpath('./a/img/@src')[0]]
# #             num = re.findall(r'\d+', li.xpath('./p[1]/text()')[0])[0]
# #             try:
# #                 resp = requests.get(url, headers=headers)
# #             except:
# #                 time.sleep(5)
# #                 resp = requests.get(url, headers=headers)
# #             text = resp.content.decode('utf-8')
# #             html = etree.HTML(text)
# #             img_pages = 1
# #             try:
# #                 img_pages = html.xpath('//*[@id="pages"]/a/text()')[-2]
# #             except:
# #                 img_pages = 1
# #             for img_page in range(1, int(img_pages) + 1):
# #                 img_url = url.replace('.html', '_%s.html' % img_page)
# #                 if img_page == 1: img_url = url
# #                 try:
# #                     resp = requests.get(img_url, headers=headers)
# #                 except:
# #                     time.sleep(5)
# #                     resp = requests.get(img_url, headers=headers)
# #                 text = resp.content.decode('utf-8')
# #                 html = etree.HTML(text)
# #                 imgs = html.xpath('//*[@class="content"]//img/@src')
# #                 for i in imgs:
# #                     img.append(i)
# #                     # print(img_url,imgs)
# #             # print(len(img))
# #             all = {'分区': frnqu_name, '所在页数': page, '图片数量': num, '标题': title, '链接': url, '图片': img}
# #             try:
# #                 print(all)
# #             except:
# #                 pass
# #
# #             # file_path = r'./美图录/%s/%s/%s/'%(frnqu_name,page,title)
# #             # if not os.path.exists(file_path):os.makedirs(file_path)
# #             # open('./美图录/%s.txt'%frnqu_name,'a+',encoding='utf-8').write(str(all)+'\n')
# #
# #             url = all['链接']
# #             id = re.findall('\d+', url)[0]
# #             if len(all['图片']) != 0:
# #                 for index, img in enumerate(all['图片']):
# #
# #                     out_dir = './美图录/all下载/%s/' % all['标题']
# #                     out_name = '%s--#--%s.jpg' % (all['标题'], str(index))
# #                     out_path = out_dir + out_name
# #                     if not os.path.exists(out_path):
# #                         try:
# #                             print('开始下载', page, img, all['标题'])
# #                         except:
# #                             print('开始下载', page, img)
# #                         text = ''
# #                         try:
# #                             text = requests.get(img).content
# #                         except:
# #                             time.sleep(5)
# #                             try:
# #                                 text = requests.get(img).content
# #                             except:
# #                                 pass
# #                         if not os.path.exists(out_dir): os.makedirs(out_dir)
# #                         try:
# #                             open(out_path, 'wb').write(text)
# #                         except:
# #                             pass
# #                     else:
# #                         print('pic已存在', page, img, all['标题'])
# import requests
# import re
# import os
#
# # 类型列表
# Type_list = {1: 'qingchun', 2: 'xiaohua', 3: 'chemo', 4: 'qipao', 5: 'mingxing', 6: 'xinggan', }
# Type_list_cn = {'qingchun': '青春美眉', 'xiaohua': '美女校花', 'chemo': '性感车模', 'qipao': '旗袍美女', 'mingxing': '明星写真',
#                 'xinggan': '性感美女'}
# # 请求头
# hd = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
# }
#
#
# # 主函数
# def main():
#     try:
#         for i in range(1, 7):
#             # 输出类型序号和名字 还有页数
#             print(f"{i}.{Type_list_cn[Type_list[i]]} 共{get_TotalPage(Type_list[i])}页")
#         # 限制输入
#         while (True):
#             Type_num = input('输入要获取的美女类型:')
#             if Type_num.isdigit():
#                 Type_num = eval(Type_num)
#                 if Type_num in range(1, 7):
#                     break
#                 else:
#                     print('请输入1-6的数字!')
#             else:
#                 print("请输入数字!")
#         # 类型
#         Type = Type_list[Type_num]
#         # 总页数
#         TotalPage = get_TotalPage(Type)
#         # 限制输入
#         while (True):
#             DownloadPage = input("请输入要获取前多少页(为空则全部):")
#             if DownloadPage == '':
#                 DownloadPage = TotalPage
#                 break
#             elif DownloadPage.isdigit():
#                 DownloadPage = eval(DownloadPage)
#                 if DownloadPage in range(1, TotalPage + 1):
#                     break
#                 else:
#                     print(f"请输入1-{TotalPage}的数字!")
#             else:
#                 print("请输入数字!")
#         pic(Type_num, Type, DownloadPage)
#     except:
#         print("程序出错!\n")
#
#
# # 获取总页数
# def get_TotalPage(Type):
#     TotalPage = 0
#     url = 'https://www.mm131.net/' + Type
#     response = requests.get(url, headers=hd)
#     response.encoding = 'gb2312'
#     TotalPage_pattern = re.compile('(?<=下一页</a><a href=\'list_)\d_\d+')
#     # 正则匹配总页数
#     match = (TotalPage_pattern.findall(response.text))
#     TotalPage = eval(match[0].split('_')[1])
#     return TotalPage
#
#
# # 下载图片总功能
# def pic(Type_num, Type, DownloadPage):
#     print("\n正在处理第1页")
#     url = 'https://www.mm131.net/' + Type
#     get_web(url, Type)
#     if DownloadPage > 1:
#         for page in range(2, DownloadPage + 1):
#             print("\n正在处理第{}页".format(page))
#             # 拼凑当前页url
#             url = 'https://www.mm131.net/' + Type + '/list_' + str(Type_num) + '_' + str(page) + '.html'
#             get_web(url, Type)
#
#
# # 获取当前页网页信息用以获取套图数量和套图num
# def get_web(url, Type):
#     response = requests.get(url, headers=hd)
#     response.encoding = 'gb2312'
#     text_pattern = re.compile('您的位置[\s\S]*?末页')
#     # 先正则匹配一次缩小范围
#     text = text_pattern.findall(response.text)
#     PicList_pattern = re.compile(f'(?<=https://www.mm131.net/{Type}/)\d+')
#     # 再用正则匹配出套图NUM
#     PicList = PicList_pattern.findall(text[0])
#     total = len(PicList)
#     print(f"这页有{total}个套图\n")
#     for i in range(1, total + 1):
#         pic_num = PicList[i - 1]
#         print(f"    正在处理第{i}个套图:")
#         # 拼凑套图页面URL
#         pic_url = 'https://www.mm131.net/' + Type + '/' + pic_num + '.html'
#         get_pic(pic_url, pic_num, Type)
#
#
# # 获取套图页面信息用以获取套图名字和图片数量
# def get_pic(pic_url, pic_num, Type):
#     response = requests.get(pic_url, headers=hd)
#     response.encoding = 'gb2312'
#     pic_name_pattern = re.compile("(?<=<h5>).+(?=</h5>)")
#     # 套图名字
#     pic_name = pic_name_pattern.findall(response.text)[0]
#     print("    套图名字:" + pic_name)
#     TotalPic_pattern = re.compile('(?<=共)\d+')
#     # 图片数量
#     TotalPic = eval(TotalPic_pattern.findall(response.text)[0])
#     print("    共{}张图片".format(TotalPic))
#     # 判断当前路径下是否存在相应目录，没有则创建
#     if os.path.exists(f'图片/{Type_list_cn[Type]}/{pic_name}') == False:
#         os.makedirs(f'图片/{Type_list_cn[Type]}/{pic_name}')
#         # 开始遍历下载图片
#         for i in range(1, TotalPic + 1):
#             # 文本进度条
#             print("\r    正在下载第{:>2}张图片{:>3}%[".format(i, round(i * 100 / (TotalPic), 1)) + "$" * i + "-" * (
#             TotalPic - i) + "]", end='')
#             # 第1个图片的referer和后面图片不一样
#             if i == 1:
#                 referer = f'https://www.mm131.net/{Type}/{pic_num}.html'
#             else:
#                 referer = f'https://www.mm131.net/{Type}/{pic_num}_{i}.html'
#             # 拼凑图片URL
#             url = f'https://img1.mmmw.net/pic/{pic_num}/{i}.jpg'
#             download_pic(i, url, pic_name, Type, referer)
#     else:
#         print("    套图已存在！", end='')
#     print("\n")
#
#
# # 下载图片
# def download_pic(i, url, pic_name, Type, referer):
#     head = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
#         'Referer': referer
#     }
#     response = requests.get(url, headers=head)
#     # 下载到对应文件夹
#     try:
#         file = open(f'./图片/{Type_list_cn[Type]}/{pic_name}/{i}.jpg', 'xb')
#         file.write(response.content)
#         file.close
#     except:
#         print("    图片已存在!")
#
#
# # 无限循环主程序
# while (True): main()
# coding=utf-8

import os,time, requests, re
from lxml import etree


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Referer': 'https://www.meitulu.com/t/changtui/',
    'Cookie': 'UM_distinctid=16f94d6dc9e568-0898b8c4c5d86b-645d7c2d-144000-16f94d6dc9f2f2; CNZZDATA1255357127=738626102-1578744969-%7C1578747140'
}

'https://www.meitulu.com/gangtai/'
main_url = 'https://www.meitulu.com/t/changtui/'
resp = requests.get(main_url, headers=headers)
text = resp.content.decode('utf-8')
html = etree.HTML(text)

print('输入数字并按回车确定：3=日韩美女（96页），4=港台美女（16页），5=国产美女（222页）：')
start = int(input('start:'))

for li in html.xpath('//ul[@class="menu"]/li')[start:start + 1]:
    frnqu_url = li.xpath('.//@href')[0]
    frnqu_name = li.xpath('./a/text()')[0]
    print(frnqu_url, frnqu_name)
    resp = requests.get(frnqu_url, headers=headers)
    text = resp.content.decode('utf-8')
    html = etree.HTML(text)
    pages = 1
    try:
        pages = html.xpath('//*[@id="pages"]/a/text()')[-2]
    except:
        pages = 1
    start_page = int(input('输入开始页数 1-%s，回车确定:' % pages))
    end_page = int(input('输入结束页数 1-%s，回车确定:' % pages))
    for page in range(start_page, int(end_page) + 1):
        detil_url = frnqu_url + '%s.html' % page
        # if detil_url == 'https://www.meitulu.com/t/fengsuniang/1.html':detil_url = frnqu_url
        if page == 1: detil_url = frnqu_url
        print(detil_url)
        try:
            resp = requests.get(detil_url, headers=headers)
        except:
            time.sleep(5)
            resp = requests.get(detil_url, headers=headers)
        text = resp.content.decode('utf-8') # content内容提取
        html = etree.HTML(text)
        for li in html.xpath('//ul[@class="img"]/li'):
            title = li.xpath('string(.//p[@class="p_title"]/a/text())')
            title = re.sub('[\/:*?"<>|]', ' ', title)
            urls = li.xpath('./p[@class="p_title"]/a/@href')[0]
            if not re.findall('https', urls):
                url = 'https://www.meitulu.com' + urls
            else:
                url = urls
            img = [li.xpath('./a/img/@src')[0]]
            num = re.findall(r'\d+', li.xpath('./p[1]/text()')[0])[0]
            try:
                resp = requests.get(url, headers=headers)
            except:
                time.sleep(5)
                resp = requests.get(url, headers=headers)
            text = resp.content.decode('utf-8')
            html = etree.HTML(text)
            img_pages = 1
            try:
                img_pages = html.xpath('//*[@id="pages"]/a/text()')[-2]
            except:
                img_pages = 1
            for img_page in range(1, int(img_pages) + 1):
                img_url = url.replace('.html', '_%s.html' % img_page)
                if img_page == 1: img_url = url
                try:
                    resp = requests.get(img_url, headers=headers)
                except:
                    time.sleep(5)
                    resp = requests.get(img_url, headers=headers)
                text = resp.content.decode('utf-8')
                html = etree.HTML(text)
                imgs = html.xpath('//*[@class="content"]//img/@src')
                for i in imgs:
                    img.append(i)
                    # print(img_url,imgs)
            # print(len(img))
            all = {'分区': frnqu_name, '所在页数': page, '图片数量': num, '标题': title, '链接': url, '图片': img}
            try:
                print(all)
            except:
                pass

            # file_path = r'./美图录/%s/%s/%s/'%(frnqu_name,page,title)
            # if not os.path.exists(file_path):os.makedirs(file_path)
            # open('./美图录/%s.txt'%frnqu_name,'a+',encoding='utf-8').write(str(all)+'\n')

            url = all['链接']
            id = re.findall('\d+', url)[0]
            if len(all['图片']) != 0:
                for index, img in enumerate(all['图片']):

                    out_dir = './美图录/all下载/%s/' % all['标题']
                    out_name = '%s--#--%s.jpg' % (all['标题'], str(index))
                    out_path = out_dir + out_name
                    if not os.path.exists(out_path):
                        try:
                            print('开始下载', page, img, all['标题'])
                        except:
                            print('开始下载', page, img)
                        text = ''
                        try:
                            text = requests.get(img).content
                        except:
                            time.sleep(5)
                            try:
                                text = requests.get(img).content
                            except:
                                pass
                        if not os.path.exists(out_dir): os.makedirs(out_dir)
                        try:
                            open(out_path, 'wb').write(text)
                        except:
                            pass
                    else:
                        print('pic已存在', page, img, all['标题'])