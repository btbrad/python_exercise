import time

class CacheDecorator:
    __cache = {}

    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args, **kwargs):
        if self.fn.__name__ in CacheDecorator.__cache:
            return CacheDecorator.__cache[self.fn.__name__]
        else:
            CacheDecorator.__cache[self.fn.__name__] = self.fn(*args, **kwargs)


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

@cost_time
@CacheDecorator
def func1_long_time():
    """模拟执行时间长，且每次返回值相同"""
    print('start func1')
    time.sleep(3)
    print('end func1')
    return 999

if __name__ == '__main__':
    func1_long_time()
    func1_long_time()
