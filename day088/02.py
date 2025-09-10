"""
题目 2：列表去重

给定一个列表，去除其中重复的元素，并保持原有顺序。
例如：

输入: [1, 2, 2, 3, 4, 3, 5]
输出: [1, 2, 3, 4, 5]
"""


def remove_duplicates(lst):
    return list(set(lst))


def remove_duplicates_2(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


if __name__ == "__main__":
    print(remove_duplicates([1, 2, 2, 3, 4, 3, 5]))
    print(remove_duplicates_2([1, 2, 2, 3, 4, 3, 5]))
