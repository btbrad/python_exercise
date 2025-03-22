import time
from time import sleep

def my_log(fn):
    print('my_log start')
    def inner(*args, **kwargs):
        print('记录日志 start')
        fn(*args, **kwargs)
        print('记录日志 end')
    print('my_log end')
    return inner

def cost_time(fn):
    print('cost time start')
    def inner():
        print('开始计时')
        start = time.time()
        fn()
        end = time.time()
        print('结束计时: ', end - start)
    print('cost time end')
    return inner

@my_log
@cost_time
def func1():
    print('func1 start')
    sleep(3)
    print('func1 end')

func1()