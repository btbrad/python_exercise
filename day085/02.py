'''
题目 2：统计元音字母

写一个函数，统计一个字符串中元音字母（a, e, i, o, u）出现的次数。
'''

def count_vowels(s):
  vowels = ['a', 'e', 'i', 'o', 'u']
  res_list = []
  for x in s:
    if x.lower() in vowels:
      res_list.append(x)
  return len(res_list)

def count_vowels_2(s):
  vowels = 'aeiou'
  count = 0
  for x in s:
    if x.lower() in vowels:
        count += 1
  return count

if __name__ == "__main__":
  print(count_vowels("banana"))
  print(count_vowels_2("banana"))