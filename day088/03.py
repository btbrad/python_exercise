"""
题目 1：斐波那契数列

写一个函数，接收一个整数 n，返回前 n 个斐波那契数列。
例如：

输入: 5
输出: [0, 1, 1, 2, 3]
"""


def fibonacci(n):
    if n <= 0:
        return []

    sequence = [0, 1]
    while len(sequence) <= n:
        next_value = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
        sequence.append(next_value)

    return sequence


if __name__ == "__main__":
    print(fibonacci(5))
