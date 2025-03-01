num = 0
while num <= 10:
    print(num, end="\t")
    num += 1

sum_result = 0
a = 0
while a <= 100:
    sum_result += a
    a += 1
print(f"1到100的和是:{ sum_result }")

sum_odd = 0
b = 1
while b <= 100:
    if b % 2 == 0:
        sum_odd += b
    b += 1
print(f"1到100奇数的和是：{ sum_odd }")