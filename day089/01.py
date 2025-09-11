"""
题目 1：列表去重

给定一个包含重复元素的列表，写一个函数去重并保持原有顺序。

输入：

nums = [1, 2, 2, 3, 1, 4, 5, 3]


输出：

[1, 2, 3, 4, 5]
"""


def remove_duplicates(nums):
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result


if __name__ == "__main__":
    nums = [1, 2, 2, 3, 1, 4, 5, 3]
    print(remove_duplicates(nums))
