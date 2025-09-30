"""
编写一个函数 is_palindrome_number(x: int) -> bool，判断一个整数是否是回文数。

负数不是回文数。
"""


def is_palindrome_number(x: int) -> bool:
    if x < 0:
        return False
    x = str(x)
    return x == x[::-1]


if __name__ == "__main__":
    print(is_palindrome_number(121))
    print(is_palindrome_number(-121))
