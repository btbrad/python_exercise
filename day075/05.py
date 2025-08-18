'''
去掉一个整数列表中的奇数，并对所有的偶数求平方得到一个新的列表
'''

def is_even(n):
  return n % 2 == 0

def square(n):
  return n * n

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = filter(is_even, list1)
square_list = map(square, even_list)

print(list(square_list))

list2 = list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, list1)))
print(list(list2))