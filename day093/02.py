"""
写一个程序：

定义一个函数 reverse_string(s)，接收一个字符串 s，返回它的反转字符串。

从用户输入一个字符串，调用函数并输出反转结果。
"""


def reverse_string(s):
    return s[::-1]


s = input("请输入一个字符串：")
print(reverse_string(s))
