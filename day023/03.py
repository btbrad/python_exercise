from queue import Queue
from threading import Thread
from time import sleep


def producer():
    num = 1
    while True:
        if queue.qsize() < 5:
            print(f"生产{num}号商品")
            queue.put(f"商品：{num}号")
            num += 1
        else:
            print("商品库已满，等待消费者！")
        sleep(1)


def consumer():
    while True:
        print(f"获取{queue.get()}")
        sleep(10)


if __name__ == '__main__':
    queue = Queue()

    t1 = Thread(target=producer)
    t2 = Thread(target=consumer)

    t1.start()
    t2.start()
