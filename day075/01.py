'''
输入一段话，统计每个英文字母出现的次数
'''
sentence = input('请输入一段话：')

count = {}
for char in sentence:
  if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
    count[char] = count.get(char, 0) + 1

for key, value in count.items():
  print(f'字母{key}出现了{value}次.')