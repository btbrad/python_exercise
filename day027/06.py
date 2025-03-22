L = [x * x for x in range(10)]
print(L)

g = (x * x for x in range(10))
print(g)

for _i in range(10):
    print(next(g))