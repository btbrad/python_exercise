'''
水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$。
'''

for num in range(100, 1000):
    # int1 = num // 100
    # int2 = (num - 100 * int1) // 10
    # int3 = num - 100 * int1 - 10 * int2
    int1 = num // 100
    int2 = num // 10 % 10
    int3 = num % 10
    if int1**3 + int2**3 + int3**3 == num:
        print(num)
