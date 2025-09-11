"""
题目 3：合并两个字典

写一个函数，合并两个字典，如果有相同的键，值相加。

输入：

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}


输出：

{"a": 1, "b": 5, "c": 4}
"""


def merge_dicts(dict1, dict2):
    result = dict1.copy()
    for k, v in dict2.items():
        result[k] = result.get(k, 0) + v
    return result


if __name__ == "__main__":
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}
    print(merge_dicts(dict1, dict2))
