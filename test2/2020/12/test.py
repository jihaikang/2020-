import requests
import lxml.html
import os
import glob


# etree = lxml.html.etree
# url = 'https://you.ctrip.com/sight/jingdezhen405/61150.html'
# response  = requests.get(url=url)
# data = etree.HTML(response.text)
# comments = data.xpath('//div[@class="commentItem"]')
# for comment in comments:
#     print(comment)
for filename in os.listdir('D:/pycharm/untitled/test2/2020/12'):
    print(filename)
a= glob.glob(r"D:/pycharm/untitled/test2/2020/12/*.j")
for b in a:
    os.remove(b)