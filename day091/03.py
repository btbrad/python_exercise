"""
题目3：字典统计

给定一个字符串，统计其中每个字符出现的次数，并以字典形式返回。
示例：

"hello" → {'h': 1, 'e': 1, 'l': 2, 'o': 1}
"""


def count_char(s):
    dict_s = {}
    for x in s:
        dict_s[x] = dict_s.get(x, 0) + 1
    return dict_s


if __name__ == "__main__":
    print(count_char("hello"))
