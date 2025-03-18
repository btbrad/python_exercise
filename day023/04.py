import os
from multiprocessing import Process
from time import sleep


def func1(name):
    print(f"{name}进程ID: {os.getpid()}")
    print(f"父进程ID: {os.getppid()}")
    print(f"进程{name}启动")
    sleep(3)
    print(f"进程{name}结束")


if __name__ == '__main__':
    print(f"当前进程ID：{os.getpid()}")
    p1 = Process(target=func1, args=("p1",))
    p2 = Process(target=func1, args=("p2",))

    p1.start()
    p2.start()