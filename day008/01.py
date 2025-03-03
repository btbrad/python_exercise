a = 100


def fun():
    b = 20
    global a
    a = 10
    print(a)
    print(a + b)
    print(locals())
    print(globals())

fun()
print(a)
