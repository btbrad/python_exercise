def f1(a, b, *c):
    print(a, b, c)


f1(1, 2, 3, 4, 5)

def f2(a, b, **c):
    print(a, b, c)


f2(1, 2, name="bt", age=30)
