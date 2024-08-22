def gys(x, y):
    max = x
    if x < y:
        max = y
    for n in range(max, 0, -1):
        if x % n == 0 and y % n == 0:
            return n

res = gys(15, 20)
print(res)

def gbs(x, y):
    return x * y
res2 = gbs(3,7)
print(res2)