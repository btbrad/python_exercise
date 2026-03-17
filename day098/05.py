"""
输入一个正整数判断它是不是素数。
素数指的是只能被1和自身整除的大于1的整数。
"""

number = int(input("请输入一个整数："))

if number <= 1:
    print(f"{number}不是素数！")
else:
    for i in range(2, number):
        if number % i == 0:
            print(f"{number}不是素数！")
            break
    else:
        print(f"{number}是素数！")
