def outer_fn(fn):
    def inner_fn(*args, **kwargs):
        print('日志...')
        fn(*args, **kwargs)

    return inner_fn


def fn1():
    print('fn1执行了')


def fn2(a, b, c):
    print(f'fn2执行了...{a},{b},{c}')


fn1 = outer_fn(fn1)
fn1()

fn2 = outer_fn(fn2)
fn2(1, 2, 3)
