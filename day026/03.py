a = 10


def add():
    a = 10

    def fn():
        nonlocal a
        a += 1
        print(f'a: {a}')

    return fn


def print_ten():
    if a == 10:
        print('a = 10')
    else:
        print('a != 10')


func1 = add()
func1()
func1()
func1()
print_ten()
