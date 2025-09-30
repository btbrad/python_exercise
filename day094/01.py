"""
编写一个函数 is_palindrome(s: str) -> bool，判断一个字符串是否为回文。

回文：正着读和反着读都一样，例如 "level"、"madam"、"12321"。

忽略大小写，例如 "RaceCar" 也算回文。
"""


def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]


def is_palindrome_2(s):
    s = s.lower()
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True


def is_palindrome3(s):
    s = s.lower()
    left, right = 0, len(s) - 1  # 双指针
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    print(is_palindrome("RaceCar"))
    print(is_palindrome("12321"))
    print(is_palindrome("level"))
    print(is_palindrome("madam"))
