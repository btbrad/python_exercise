class MyLog:

    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args, **kwargs):
        print('记录日志')
        return self.fn(*args, **kwargs)

@MyLog
def func1():
    print('执行func2!')


if __name__ == '__main__':
    func1()
