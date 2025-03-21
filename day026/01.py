import functools

add_func = lambda x, y: x + y

print(add_func(2, 7))

g = [lambda a: a * 2, lambda b: b * 3, lambda c: c * 4]
print(g[0](2))
print(g[1](2))
print(g[2](2))

int8 = functools.partial(int, base=8)
print(int8('1010'))