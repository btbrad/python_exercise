res1 = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])
print(list(res1))

res2 = filter(lambda x: x and x.strip(), ['A', ' ', 'B', '   ', 'C'])
print(list(res2))

res3 = sorted([3, 1, 8, 4, 2])
print(res3)

res4 = sorted([-9, 1, -8, -4, 2], key=abs)
print(res4)