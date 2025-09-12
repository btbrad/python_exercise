"""
题目2：判断回文字符串

编写一个函数 is_palindrome(s)，判断输入字符串 s 是否为回文（正读和反读都一样，忽略大小写和空格）。

示例：

is_palindrome("A man a plan a canal Panama")  # 输出: True
is_palindrome("hello")                       # 输出: False
"""


def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]


def is_palindrome2(s):
    s = s.lower().replace(" ", "")
    list_s = list(s.lower())
    list_s_reverse = list_s[::-1]
    return list_s == list_s_reverse


if __name__ == "__main__":
    print(is_palindrome("A man a plan a canal Panama"))  # 输出: True
    print(is_palindrome("hello"))  # 输出: False
    print(is_palindrome2("A man a plan a canal Panama"))  # 输出: True
    print(is_palindrome2("hello"))  # 输出: False
