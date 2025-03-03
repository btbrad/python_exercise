list_a = [10, 20]

def f1(m):
    print(id(m))
    m.append(30)
    print(id(m))

f1(list_a)

print(id(list_a))
print(list_a)

int_a = 100

def f2(n):
    print(f"n: { id(n) }")
    n += 1
    print(f"n: { id(n) }")
    print(n)

f2(int_a)

print(id(int_a))
print(int_a)

print("--------------------------------")
list_b = (10, 20, [5, 6])
print(f"list_b: { id(list_b) }")
def f3(m):
    print(id(m))
    m += (30, 40)
    m[2][0] = 888
    print(id(m))

f3(list_b)

print(f"list_b: {id(list_b)}")
print(list_b)