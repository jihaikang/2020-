# coding = utf-8
from socket import *

udp_socket = socket(AF_INET,SOCK_DGRAM)
dest_addr = ('127.0.0.1',8080)
send_data = input("请输入要发送的数据：")
udp_socket.sendto(send_data.encode('utf-8'),dest_addr)
udp_socket._closed()