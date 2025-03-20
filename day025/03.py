from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread


def recv_data():
    print('等待接收数据:')
    while True:
        recv_data = s.recvfrom(1024)
        recv_content = recv_data[0].decode("gbk")
        print(f'收到远程信息:{recv_content}, 来自: {recv_data[1]}')
        if recv_content == '88':
            print('结束通信！')
            s.close()
            break


def send_data():
    addr = ('127.0.0.1', 8888)
    while True:
        data = input('请输入：')
        s.sendto(data.encode('gbk'), addr)
        if data == '88':
            print('结束聊天！')
            break


if __name__ == '__main__':
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(('127.0.0.1', 9999))

    t1 = Thread(target=recv_data)
    t2 = Thread(target=send_data)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
