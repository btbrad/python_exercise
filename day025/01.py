from socket import *

s = socket(AF_INET, SOCK_DGRAM)
addr = ('127.0.0.1', 9527)

while True:
    data = input('请输入：')
    s.sendto(data.encode('gbk'), addr)
    if data == '88':
        print('结束聊天！')
        break

s.close()