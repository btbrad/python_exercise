def my_log(fn):
    def inner(*args, **kwargs):
        fn(*args, **kwargs)
        print("记录日志")
    return inner

@my_log
def func1():
    print("func1执行了！")

@my_log
def func2(a, b):
    print("func2执行了！", a, b)


#func1 = outer(func1)
#func2 = outer(func2)

func1()
func2(1, 2)
