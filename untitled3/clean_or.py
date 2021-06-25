import requests
from bs4 import BeautifulSoup
url = "http://www.cntour.cn/"
st = requests.get(url)
soup = BeautifulSoup(st.text,'lxml')
data = soup.select(' head > title')  # select获取失败
print(data)

