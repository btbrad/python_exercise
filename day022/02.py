from threading import Thread
from time import sleep


class MyThread(Thread):

    def __init__(self, name):
        super(MyThread, self).__init__()
        self.name = name

    def run(self):
        print(f"线程{self.name}启动")
        for i in range(3):
            print(f"线程{self.name}运行: {i}")
        sleep(3)
        print(f"线程{self.name}结束")



if __name__ == '__main__':
    print("主线程启动")
    t1 = MyThread("t1")
    t2 = MyThread("t2")
    t3 = MyThread("t3")

    t3.daemon = True

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()

    print("主线程结束")
