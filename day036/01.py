data = [1, 2, 3, 4, 5, 6, 7, 8]
evens = [x for x in data if x % 2 == 0]
print(evens)

data2 = [1, 'one', 2, 'two', 3, 'three', 4, 'four']
words = [x for x in data2 if isinstance(x, str)]
print(words)

data3 = list('So long and thanks for all the fish'.split())
title = [x.title() for x in data3]
print(title)