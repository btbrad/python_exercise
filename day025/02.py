from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('127.0.0.1', 9527))

print('等待接收数据:')
while True:
    recv_data = s.recvfrom(1024)
    recv_content = recv_data[0].decode("gbk")
    print(f'收到远程信息:{recv_content}, 来自: {recv_data[1]}')
    if recv_content == '88':
        print('结束通信！')
        s.close()
        break


