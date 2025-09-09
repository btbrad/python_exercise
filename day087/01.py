"""
题目 1：回文字符串

写一个函数，判断一个字符串是否为回文（正着读和反着读一样）。
示例：

"madam" → True

"hello" → False
"""


def is_palindrome(s):
    list_s = list(s)
    reversed_list = list_s[::1]
    reversed_list.reverse()
    length = len(list_s)
    for i in range(length):
        if length % 2 == 0:
            if list_s[i] != reversed_list[i]:
                return False
        else:
            if (i != length // 2 + 1) and list_s[i] != reversed_list[i]:
                return False
    return True


def is_palindrome2(s):
    s = s.lower()
    return s == s[::-1]


def is_palindrome3(s):
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return False
    return True


if __name__ == "__main__":
    print(is_palindrome("madam"))
    print(is_palindrome2("madam"))
    print(is_palindrome3("madam"))
