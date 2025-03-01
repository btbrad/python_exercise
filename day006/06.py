a = [1, 2, 3, 4, 5]
for x in a:
    print(x, end="\t")

b = (1, 2, 3, 4, 5)
for x in b:
    print(x, end="\t")

c = { "name": "bt", "age": 18, "gender": "male" }
for x in c:
    print(x, end="\t")
for x in c.keys():
    print(x, end="\t")
for x in c.values():
    print(x, end="\t")
for x in c.items():
    print(x, end="\t")

sum_all = 0
sum_odd = 0
sum_even = 0
for x in range(1, 101):
    sum_all += x
    if x % 2 == 0:
        #偶数
        sum_even += x
    else:
        #奇数
        sum_odd += x

print(f"1到100的和是：{ sum_all }, 偶数和是：{ sum_even }, 奇数和是：{ sum_odd }.")