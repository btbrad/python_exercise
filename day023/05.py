import os
from multiprocessing import Process
from time import sleep


class MyProcess(Process):

    def __init__(self, name):
        super(MyProcess, self).__init__()
        self.name = name

    def run(self):
        print(f"{self.name}进程ID: {os.getpid()}")
        print(f"父进程ID: {os.getppid()}")
        print(f"进程{self.name}启动")
        sleep(3)
        print(f"进程{self.name}结束")

if __name__ == '__main__':
    print(f"当前进程ID：{os.getpid()}")
    p1 = MyProcess("p1")
    p2 = MyProcess("p2")

    p1.start()
    p2.start()