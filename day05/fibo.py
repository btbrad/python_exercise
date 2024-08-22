a = 1
b = 1
for _ in range(20):
    # a, b = b, a + b
    if _ < 1:
        print(1 , end='')
    else:
        a = b
        b = a + b
        print(a, end=' ')