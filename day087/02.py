"""
题目 2：列表去重并排序

给定一个包含重复数字的列表，返回去重后并升序排序的新列表。
示例：

输入 [4, 2, 7, 2, 4, 9]

输出 [2, 4, 7, 9]
"""


def remove_duplicates_and_sort(lst):
    return sorted(set(lst))


def remove_duplicates_and_sort2(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return sorted(unique_list)


def remove_duplicates_and_sort3(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    for i in range(len(unique_list)):
        for j in range(len(unique_list) - i - 1):
            if unique_list[j] > unique_list[j + 1]:
                unique_list[j + 1], unique_list[j] = (
                    unique_list[j],
                    unique_list[j + 1],
                )
    return unique_list


if __name__ == "__main__":
    print(remove_duplicates_and_sort([4, 2, 7, 2, 4, 9]))
    print(remove_duplicates_and_sort2([4, 2, 7, 2, 4, 9]))
    print(remove_duplicates_and_sort3([4, 2, 7, 2, 4, 9]))
