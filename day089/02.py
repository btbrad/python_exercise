"""
题目 2：统计字符串单词数

写一个函数，输入一个英文句子，统计其中的 单词数量。
（单词之间可能有多个空格）

输入：

s = "  Python   is   very   good  "


输出：

4
"""

import re


def count_words(s):
    words = re.findall(r"\b\w+\b", s)
    return len(words)


def count_words2(s):
    # split() 默认会按空格分割，并自动去掉多余空格
    words = s.split()
    return len(words)


if __name__ == "__main__":
    s = "  Python   is   very   good  "
    print(count_words(s))
    print(count_words2(s))
