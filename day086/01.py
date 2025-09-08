"""
题目 1：平方数列表

写一个程序，输入一个整数 n，生成一个包含从 1 到 n 的平方数的列表。

示例：

输入: 5
输出: [1, 4, 9, 16, 25]
"""


def generate_square_numbers(n):
    return [i**2 for i in range(1, n + 1)]


if __name__ == "__main__":
    print(generate_square_numbers(5))
