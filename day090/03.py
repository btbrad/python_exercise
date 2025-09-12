"""
题目3：生成指定范围内的平方列表

编写一个函数 squares_list(start, end)，返回从 start 到 end（含）的整数的平方组成的列表。

示例：

squares_list(1, 5)  # 输出: [1, 4, 9, 16, 25]
"""


def squares_list(start, end):
    squares = []
    for i in range(start, end + 1):
        squares.append(i**2)
    return squares


def squares_list_2(start, end):
    return [i**2 for i in range(start, end + 1)]


def squares_list_3(start, end):
    return list(map(lambda x: x**2, range(start, end + 1)))


if __name__ == "__main__":
    print(squares_list(1, 5))
    print(squares_list_2(1, 5))
    print(squares_list_3(1, 5))
