from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('127.0.0.1', 9527))

print('等待接收数据')
recv_data = s.recvfrom(1024)
print(f'收到远程信息:{ recv_data[0] }, 来自: { recv_data[1] }')
s.close()