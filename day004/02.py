import random

a = [10, 20, 30, 40, 50]

for x in a:
    if x != 50:
        print(x, end=",")
    else:
        print(x)

b = [] + a
print(b)

a.sort(reverse=True)
print(a)
a.sort()
print(a)

random.shuffle(a)
print(a)

c = sorted(a) #创建新列表
print(c)
print(a)

a.sort()
print(a)

print(max(a))
print(min(a))
print(sum(a))