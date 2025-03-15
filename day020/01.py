from math import ceil
from re import sub

# 1.数组再分组
def chunk(lst, size):
  return list(map(lambda x: lst[x * size: (x + 1) * size],list(range(0, int(ceil(len(lst) / size))))))

res1 = chunk([1, 2, 3, 4, 5], 2)
print(res1) # [[1, 2], [3, 4], [5]]


# 2. 数字转数组
def digitize(n):
  return list(map(int, str(n)))

res2 = digitize(123)
print(res2) # [1, 2, 3]


# 3. 非递归斐波那契
def fibonacci(n):
  if n <= 0:
    return [0]
  
  sequence = [0, 1]
  while len(sequence) <= n:
    next_value = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
    sequence.append(next_value)

  return sequence

res3 = fibonacci(7)
print(res3) # [0, 1, 1, 2, 3, 5, 8, 13]

# 4.下划线化字符串
def snake(s):
  return '-'.join(sub('([A-Z][a-z]+)', r' \1', sub('([A-Z]+)', r' \1', s.replace('-', ' '))).split()).lower()

res4 = snake('Hello_World hola')
print(res4) # hello_-world-hola