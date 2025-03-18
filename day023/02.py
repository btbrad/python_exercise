from threading import Event, Thread
from time import sleep


def have_hotpot(name):
    print(f"{name}已经启动")
    print(f"{name}已经进入就餐状态")
    sleep(1)
    event.wait()
    print(f"{name}收到通知了")
    print(f"{name}开始吃咯")


if __name__ == '__main__':
    event = Event()

    t1 = Thread(target=have_hotpot, args=("t1",))
    t2 = Thread(target=have_hotpot, args=("t2",))

    t1.start()
    t2.start()

    sleep(10)

    print("***********主线程通知小伙伴，开吃咯")
    event.set()

