"""
编写一个函数 char_count(s: str) -> dict，返回字符串中每个字符出现的次数。

例如：

print(char_count("hello"))
# 输出: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
"""


def char_count(s):
    dict_s = {}
    for ch in s:
        dict_s[ch] = dict_s.get(ch, 0) + 1
    return dict_s


if __name__ == "__main__":
    print(char_count("hello"))
