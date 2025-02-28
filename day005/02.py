a = (10, 20, 30)
b = (100,)
c = tuple(range(3))

print(type(a))
print(type(b))
print(c, type(c))

d = (30, 10, 50, 80)
e = sorted(d)
print(type(e), e)

f = (x for x in range(10))
print(type(f))
g = tuple(f)
print(g)
h = tuple(f) #空元组
print(h)