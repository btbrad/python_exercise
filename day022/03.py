from threading import Thread, Lock
from time import sleep


class Account:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance



class Withdraw(Thread):

    def __init__(self, account, amount):
        super(Withdraw, self).__init__()
        self.account = account
        self.amount = amount

    def run(self):
        lock1.acquire()
        if self.account.balance < self.amount:
            print("账户余额不足！")
            return
        sleep(1)
        self.account.balance -= self.amount
        lock1.release()
        print(f"账户{self.account.name}, 取了{self.amount}")
        print(f"账户{self.account.name}余额{self.account.balance}")



if __name__ == '__main__':
    a = Account("卡1", 100)

    lock1 = Lock()

    t1 = Withdraw(a, 80)
    t2 = Withdraw(a, 80)

    t1.start()
    t2.start()