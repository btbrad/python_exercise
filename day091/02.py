"""
题目2：回文字符串

判断一个字符串是否为回文（正着读和反着读都一样），是则返回 True，否则返回 False。
示例：

"level" → True

"hello" → False
"""


def is_palindrome(s):
    return s == s[::-1]


if __name__ == "__main__":
    print(is_palindrome("level"))  # 输出：True
    print(is_palindrome("hello"))  # 输出：False
