"""
打印100以内的素数。
说明：素数指的是只能被1和自身整除的正整数（不包括1）。
"""

for num in range(2, 101):
    for factor in range(2, num):
        if num % factor == 0:
            break
    else:
        print(num)
