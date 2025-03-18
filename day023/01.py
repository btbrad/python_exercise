from threading import Semaphore, Thread
from time import sleep


def home(name, se):
    se.acquire()
    print(f"{name}进入房间")
    sleep(3)
    print(f"{name}离开房间")
    se.release()

if __name__ == '__main__':
    se = Semaphore(2)
    for i in range(7):
        t = Thread(target=home, args=(f"t{i}", se))
        t.start()
