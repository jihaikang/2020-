# # 实现提供时间日期的服务器
# from socket import socket, SOCK_STREAM, AF_INET
# from datetime import datetime
#
#
# def main():
#     # 1.创建套接字对象并指定使用哪种传输服务
#     # family=AF_INET - IPv4地址
#     # family=AF_INET6 - IPv6地址
#     # type=SOCK_STREAM - TCP套接字
#     # type=SOCK_DGRAM - UDP套接字
#     # type=SOCK_RAW - 原始套接字
#     server = socket(family=AF_INET, type=SOCK_STREAM)
#     # 2.绑定IP地址和端口(端口用于区分不同的服务)
#     # 同一时间在同一个端口上只能绑定一个服务否则报错
#     server.bind(('192.168.1.2', 6789))
#     # 3.开启监听 - 监听客户端连接到服务器
#     # 参数512可以理解为连接队列的大小
#     server.listen(512)
#     print('服务器启动开始监听...')
#     while True:
#         # 4.通过循环接收客户端的连接并作出相应的处理(提供服务)
#         # accept方法是一个阻塞方法如果没有客户端连接到服务器代码不会向下执行
#         # accept方法返回一个元组其中的第一个元素是客户端对象
#         # 第二个元素是连接到服务器的客户端的地址(由IP和端口两部分构成)
#         client, addr = server.accept()
#         print(str(addr) + '连接到了服务器.')
#         # 5.发送数据
#         client.send(str(datetime.now()).encode('utf-8'))
#         # 6.断开连接
#         client.close()
#
#
# if __name__ == '__main__':
#     main()
# 实现TCP客户端的功能
# from socket import socket
#
#
# def main():
#     # 1.创建套接字对象默认使用IPv4和TCP协议
#     client = socket()
#     # 2.连接到服务器(需要指定IP地址和端口)
#     client.connect(('192.168.1.2',6789))
#     # 3.从服务器接受数据
#     print(client.recv(1024).decode('utf-8'))
#     client.close()
#
#
# if __name__ == '__main__':
#     main()
# 多线程技术处理多个用户请求的服务器
# from socket import socket,SOCK_STREAM,AF_INET
# from base64 import b64encode
# from json import dumps
# from threading import Thread
#
#
# def main():
#
#     # 自定义线程
#     class FileTransferHandler(Thread):
#
#         def __init__(self,cclient):
#             super().__init__()
#             self.cclient= cclient
#
#         def run(self):
#             my_dict = {}
#             my_dict['filename'] = 'ball.png'
#             # JSON是纯文本不能携带二进制数据
#             # 所以图片的二进制数据要处理成base64编码
#             my_dict['filename'] = data
#             # 通过dumps函数将字典处理成JSON字符串
#             json_str = dumps(my_dict)
#             # 发送JSON字符串
#             self.cclient.end(json_str.encode('utf-8'))
#             self.cclient.close()
#
#     # 1.创建套接字对象并指定使用哪种传输服务
#     serve = socket()
#     # 2.绑定IP地址和端口(区分不同的服务)
#     serve.bind(('192.168.1.2',5566))
#     # 3.开启监听 - 监听客户端连接到服务器
#     serve.listen(512)
#     print('服务器启动开始监听....')
#     with open('ball.png','rb') as f:
#         # 将二进制数据处理成base64在解码成字符串
#         data = b64encode(f.read()).decode('utf-8')
#     with True:
#         client,addr = serve.accept()
#         # 启动一个线程来处理客户端的请求
#         FileTransferHandler(client).start()
#
#
# if __name__ == '__main__':
#     main()
# 客户端代码
# from socket import socket
# from json import loads
# from base64 import b64decode
#
#
# def main():
#     client = socket()
#     client.connect(('192.168.1.2',5566))
#     # 定义一个保存二进制数据的对象
#     in_data = bytes()
#     # 由于不知道服务器发送的数据有多大每次接收1024字节
#     data = client.recv(1024)
#     while data:
#         # 将收到的数据拼接起来
#         in_data += data
#         data = client.recv(1024)
#
#     # 将收到的二进制编码成JSON字符串并转换成字典
#     # loads函数的作用就是将JSON字符串转成字典对象
#     my_dict = loads(in_data.decode('utf-8'))
#     filename = my_dict['filename']
#     filedata = my_dict['filedata'].encode('utf-8')
#     with open('./' + filename,'wb') as f:
#         # 将base64格式的数据解码成二进制数据并写入文件
#         f.write(b64decode(filedata))
#     print('图片已保存')
#
#
# if __name__  == '__main__':
#     main()
# 发送邮件要使用SMTP（简单邮件传输协议）
# 而Python中的smtplib模块将这些操作简化成了几个简单的函数
# from smtplib import SMTP
# from email.header import Header
# from email.mime.text import MIMEText
#
#
# def main():
#     # 请自行修改下面的邮件发送者和接收者
#     sender = '2993431608@qq.com'
#     receivers = ['2415647901@qq.com','123456@qq.com']
#     message = MIMEText('用Python发送邮件的示例代码.','plain','utf-8')
#     message['From'] = Header('王大锤','utf-8')
#     message['To'] =Header('小白','utf-8')
#     message['Subject'] = Header('示例代码实验邮件','utf-8')
#     smtper = SMTP('smtp.qq.com')
#     # 请自行修改下面的登录口令
#     smtper.login(sender,'dxhwmzhzexxvddhd')
#     smtper.sendmail(sender,receivers,message.as_string())
#     print('邮件发送完成')
#
#
# if __name__ == '__main__':
#     main()
# 发送带有附件的邮件
# 不知道如何发图片，图片的类型
# from smtplib import SMTP
# from email.header import Header
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from email.mime.multipart import MIMEMultipart
#
# import urllib
#
# def main():
#     # 创建一个带附件的邮件消息对象
#     message = MIMEMultipart()
#
#     # 创建文本内容
#     text_content = MIMEText('附件中有本月数据请查收','plain','utf-8')
#     message['Subject'] = Header('本月数据','utf-8')
#     # 将文本内容添加到邮件发送消息对象中
#     message.attach(text_content)
#
#     # 读取文件并将文件作为附件添加到邮件消息对象中
#     with open('cb008e9d0f832a1be148b033a538d573.jpg','rb')as f:
#         img =MIMEImage(f.read(),'base64','utf-8')
#         img['Content-Type'] = 'image/plain'
#         img['Content-Type'] = 'attachment';filename = 'cb008e9d0f832a1be148b033a538d573.jpg'
#     # 读取文件并将文件作为附件添加到邮件消息对象中
#     with open('cb008e9d0f832a1be148b033a538d573.jpg','rb')as f:
#         img =MIMEImage(f.read(),'base64','utf-8')
#         img['Content-Type'] = 'application/vad.ms-image'
#         img['Content-Disposition'] ='attachment;filename=meinv-haha.jpg'
#         message.attach(img)
#
#
#     # 创建SMTP对象
#     smtper = SMTP('smtp.qq.com')
#     # 开启安全连接
#     # smtper.starttls()
#     sender = '2993431608@qq.com'
#     recivers = ['2415647901@qq.com','2993431608@qq.com']
#     # 登录到SMTP服务器
#     # 请注意此处不是使用密码而是邮件客户端授权码进行登录
#     smtper.login(sender,'dxhwmzhzexxvddhd')
#     # 发送邮件
#     smtper.sendmail(sender,recivers)
#     # 与邮件服务器断开连接
#     smtper.quit()
#     print('发送完成')
#
# if __name__ == '__main__':
#     main()
