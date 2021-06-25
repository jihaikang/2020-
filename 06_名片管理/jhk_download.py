# 三种常用的下载方式
import urllib

# import urllib2
import requests
#方法一
# print('dowmload with urllib')
url = "https://vip.d0.baidupan.com/file/?VDJTbQw9ADFVXFZuV2JSPlFuBDxQ6gaBUeVTsVSyU9wC5VOOCOwGtwf1U69U5geTA8AG51G2BYkL5VXMU6YE4FTPU7kMuQDEVatW5le4UvJR7QSUUJYG41HMU9FU7FPtAqNT4AjuBuIHtFOAVLEH4wPJBo9RUQXgC5BV0lPoBJBU8VNbDLQA0VWyVuVXk1LfUe8EvFCcBuFRxFPZVOFTzQKrU+EIzgbvB7lTlFSbB+AD+waGUegFswuSVbpTjAS4VLFTpAzTALxVtlabV+RS9lGVBOVQtwa+UbJT7VSlU7cCvVOHCAoGugfkU7BU5ge2A+EG5lGqBa0LIlUjU2sEY1RyU2IMOAA4VWZWX1dqUjdRNgQyUD8GM1FiU2JUO1NqAjFTIggzBiEHbFMwVDMHMgNtBjNRNwUhC3xVI1MyBDdUZFM2DGEAe1UyVjBXLFJjUTMELlA2BjdRN1MxVGtTYQJmU2IIbQZiB2dTPVRmB2UDOgZnUTYFNQtoVWJTbAQ8VGRTPAw3ADZVYlY4VzRSalFqBGBQIQZ0UTJTM1QuUycCcVNhCCcGOwc1UzhUMQcyA2EGMlE4BTMLNVV1U3sEbFQ5U2EMNwBpVTJWNlczUmZROgQ1UDcGMFFhU2RUJlN0AndTdAhoBmMHf1MjVGYHagMuBj5RPwUxCzxVYVM7BDNUZ1MwDGUAY1UlVnVXc1IkUTYEMFA5BjRRZFNkVD9TYwI2Uz0IYAZ0ByRTbFRwBzsDaAYyUTkFKQs9VWRTNwQrVG1TNwx/AGVVNFY2"
# urllib.urlretrieve(url,"lanzous")  不行， module 'urllib' has no attribute 'urlretrieve'
# 方法二  此方法python常用
r = requests.get(url)
with open("lanzo"+".pdf","wb") as f:
    f.write(r.content)# No,rite() argument must be str, not bytes
#方法三
# print ('downloading with urllib2')
# url = 'http://www.pythontab.com/test/demo.zip'
# f = urllib2.urlopen(url)
# data = f.read()
# with open("demo2.zip", "wb") as code:
#     code.write(data)