"""
题目 3：统计单词出现次数

写一个函数，接收一段英文句子，返回每个单词出现的次数（忽略大小写和标点符号）。
示例：

输入 "Hello, hello world!"

输出 {"hello": 2, "world": 1}
"""

import re
from collections import Counter


def count_word_occurrences(sentence):
    sentence = sentence.lower()
    words = re.findall(r"\b\w+\b", sentence)
    return dict(Counter(words))


def count_word_occurrences2(sentence):
    sentence = sentence.lower()
    words = sentence.split()
    clean_words = [w.strip(".,!?;\"'()[]{}") for w in words]
    res_dict = {}
    for w in clean_words:
        if w:
            res_dict[w] = res_dict.get(w, 0) + 1
    return res_dict


if __name__ == "__main__":
    s = "Hello, hello world!"
    print(count_word_occurrences(s))
    print(count_word_occurrences2(s))
