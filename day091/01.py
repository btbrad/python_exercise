"""
题目1：列表去重

编写一个函数，接收一个包含重复数字的列表，返回一个去重后的新列表（保持原有顺序）。
"""


def remove_duplicates(lst):
    set_1 = set()
    result = []
    for item in lst:
        if item not in set_1:
            set_1.add(item)
            result.append(item)
    return result


if __name__ == "__main__":
    print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # 输出：[1, 2, 3, 4, 5]
