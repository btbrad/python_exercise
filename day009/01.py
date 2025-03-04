eval("print('hello world')")

a = 1
b = 2
c = eval("a+b")
print(c)

d1 = dict(a=10,b=20)
d = eval("a+b", d1)
print(d)