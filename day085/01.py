'''
题目 1：字符串反转

写一个函数，输入一个字符串，返回这个字符串的反转结果。
'''
def reverse_string(s):
  return s[::-1]

def reverse_string_2(s):
  return ''.join(reversed(s))

def reverse_string_3(s):
  list_s = [x for x in s]
  list_s.reverse()
  return ''.join(list_s)

def reverse_string_4(s):
  list_s = [x for x in s]
  list_s = sorted(list_s, reverse=True)
  return ''.join(list_s)


if __name__ == "__main__":
    print(reverse_string("abcdefg"))
    print(reverse_string_2("abcdefg"))
    print(reverse_string_3("abcdefg"))
    print(reverse_string_4("abcdefg"))