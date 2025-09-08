"""
题目 2：字典反转

给定一个字典，把它的 键和值对调，生成一个新的字典。

示例：

输入: {"a": 1, "b": 2, "c": 3}
输出: {1: "a", 2: "b", 3: "c"}
"""


def invert_dictionary(d):
    new_dict = {}
    for k, v in d.items():
        new_dict[v] = k
    return new_dict


def invert_dictionary2(d):
    return {v: k for k, v in d.items()}


if __name__ == "__main__":
    print(invert_dictionary({"a": 1, "b": 2, "c": 3}))
    print(invert_dictionary2({"a": 1, "b": 2, "c": 3}))
