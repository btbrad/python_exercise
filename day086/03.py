"""
题目 3：统计单词出现次数

写一个程序，输入一句英文句子，统计每个单词出现的次数，并用字典存储。

示例：

输入: "apple banana apple orange banana apple"
输出: {"apple": 3, "banana": 2, "orange": 1}
"""


def count_word_occurrences(sentence):
    word_list = sentence.split(" ")
    word_dict = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict


if __name__ == "__main__":
    s = "apple banana apple orange banana apple"
    print(count_word_occurrences(s))
