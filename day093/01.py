"""
写一个程序：

定义一个函数 is_even(n)，判断一个整数 n 是否是偶数。

从用户输入一个整数，调用 is_even 函数判断，并打印结果：

如果是偶数，输出 "n 是偶数"

如果是奇数，输出 "n 是奇数"
"""


def is_even(n):
    return n % 2 == 0


n = int(input("请输入一个整数："))
if is_even(n):
    print(f"{n}是偶数")
else:
    print(f"{n}是奇数")
