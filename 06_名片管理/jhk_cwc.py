#爬取网页内容
#方法一
# import urllib.request
# url = "http://www.pythontab.com"
# html = urllib.request.urlopen(url).read() # 最基础的抓取
# print(html)
#方法二
import requests
url = "http://www.python.com"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
             'Accept':'text/html;q=0.9,*/*;q=0.8',
             'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
             'Accept-Encoding':'gzip',
             'Connection':'close',
             'Referer':None #注意如果依然不能抓取，这里可以设置抓取网站的host
             }
html =requests.get(url,headers=headers)
html.encoding = html.apparent_encoding# 方法二运行失败