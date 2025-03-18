from multiprocessing import Process, Queue, set_start_method
from time import sleep


class MyProcess(Process):

    def __init__(self, name, queue_ins):
        super(MyProcess, self).__init__()
        self.name = name
        self.queue = queue_ins

    def run(self):
        print(f"进程{self.name}启动了")
        print(f"获取数据: {self.queue.get()}")
        sleep(3)
        print(f"进程{self.name}结束了")


if __name__ == '__main__':

    set_start_method("fork")

    queue = Queue()
    queue.put("1")
    queue.put("2")
    queue.put("3")

    p_list = []
    for i in range(3):
        p = MyProcess(f"P{i + 1}", queue)
        p_list.append(p)
    for process in p_list:
        process.start()
