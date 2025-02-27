"""
列表
"""
a = [20, 30, 'bt']
print(a)

b = list(range(10))
print(b)

c = [x * 2 for x in range(1, 100) if x % 3 == 0]
print(c)

a.append(40) #推荐使用
print(a)

print(id(a))
a = a + [50] #会创建新的列表对象
print(a)
print(id(a))

d = [60, 70]
a.extend(d) #添加到尾部，不创建新的对象
print(a)

a.insert(0,10)
print(a)

e = a * 3 #创建新的对象
print(e)

del a[3]
print(a)

deleted_element = a.pop()
print(a, deleted_element)

a.remove(30)
print(a)

print(a[2])
print(a.index(20))
print(a.count(60))
print(len(a))
print(70 in a)
print(20 not in a)

print(a[2:4])
print(a[-3:-1])
print(a[-2:-4:-1])
print(a[::-1])