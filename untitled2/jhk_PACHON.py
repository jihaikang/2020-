# import requests
#
#
# url = 'https://www.52pojie.cn/forum.php'
# web_data = requests.get(url)
# pj_data = web_data.text
# print(pj_data)
# import requests
# from bs4 import BeautifulSoup
#
#
#
# for i in range(0,980,20):
#     url = 'https://book.douban.com/tag/历史?start=%d&type=T'% i
#     douban_data = requests.get(url)
#     soup = douban_data.text
#     if i == 80:
#         break
#     print(soup)


    # titles = soup.select('subject_list > ul > li > div.info > h2 > a')
    # prices = soup.select('div.pub')
    # stars = soup.select('#subject_list >ul > li > div.info > '
    #                     'div.star.clearfix > span.rating_nums')
    # for title,price,star in zip(titles,prices,stars):
    #     data = {
    #         'title': title.get_text(),
    #         'price': price.get_text(),
    #         'star': star.get_text()
    #     }
    #     print(data)
# for i in range(1, 10):
#     print(i)
#     while True:
#         if i < 8:
#             print(i)
#             break
#         else:
#             i += 2
#             print(i)
#
# print('结束')
numbers = [1,2,3,4,5]
for n in numbers:
    if (n > 5):
        print('the value is %d '%(n))
        break
else:
    print('the for loop does not end with break')
i = 0
while(numbers[i] < 5):
    print('the index %d value is %d'%(i, numbers[i]))
    if (numbers[i] < 0) :
        break
    i = i + 1
else:
    print('the loop does not end with break')