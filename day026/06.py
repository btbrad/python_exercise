from functools import reduce

add_sum = reduce(lambda x, y : x + y, [1, 2, 3, 4, 5])
print(add_sum)