"""
题目 1：反转字符串

编写一个函数，接收一个字符串，返回反转后的结果。
例如：

输入: "hello"
输出: "olleh"
"""


def reverse_string(s):
    return s[::-1]


def reverse_string_2(s):
    list_s = list(s)
    list_s.reverse()
    return "".join(list_s)


def reverse_string_3(s):
    list_s = list(s)
    length = len(list_s)
    reversed_list = []
    for i in range(length):
        reversed_list.append(list_s[length - 1 - i])
    return "".join(reversed_list)


def reverse_string_4(s):
    list_s = list(s)
    length = len(list_s)
    reversed_list = []
    for i in range(length):
        reversed_list.append(list_s.pop())
    return "".join(reversed_list)


if __name__ == "__main__":
    print(reverse_string("hello"))
    print(reverse_string_2("hello"))
    print(reverse_string_3("hello"))
    print(reverse_string_4("hello"))
