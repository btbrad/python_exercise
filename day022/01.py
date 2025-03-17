from threading import Thread
from time import sleep


def func1(name):
    print(f"线程{name}启动")
    for i in range(3):
        print(f"线程{name}运行: {i}")
    sleep(3)
    print(f"线程{name}结束")


if __name__ == '__main__':
    print("主线程启动")
    t1 = Thread(target=func1, args=("t1",))
    t2 = Thread(target=func1, args=("t2",))

    t1.start()
    t2.start()

    print("主线程结束")
