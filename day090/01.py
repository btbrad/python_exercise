"""
题目1：统计列表中偶数和奇数的个数

给定一个整数列表 nums，统计其中偶数和奇数的数量，并输出结果。

示例：

nums = [1, 2, 3, 4, 5, 6]
# 输出：
# 偶数个数: 3
# 奇数个数: 3
"""


def count_even_odd(nums):
    even_count = 0
    odd_count = 0

    for num in nums:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print(f"偶数个数: {even_count}")
    print(f"奇数个数: {odd_count}")


def count_even_odd_2(nums):
    dict_num = {}
    for num in nums:
        dict_num[num % 2] = dict_num.get(num % 2, 0) + 1

    print(f"偶数个数: {dict_num[0]}")
    print(f"奇数个数: {dict_num[1]}")


def count_even_odd_3(nums):
    even_count = sum(1 for num in nums if num % 2 == 0)
    odd_count = sum(1 for num in nums if num % 2 != 0)

    print(f"偶数个数: {even_count}")
    print(f"奇数个数: {odd_count}")


if __name__ == "__main__":
    count_even_odd([1, 2, 3, 4, 5, 6])
    count_even_odd_2([1, 2, 3, 4, 5, 6])
    count_even_odd_3([1, 2, 3, 4, 5, 6])
