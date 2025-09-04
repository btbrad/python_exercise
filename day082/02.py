fruits = ['apple', 'orange', 'mango', 'banana']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
print('-------------------------')

nums = [5, 2, 9, 1]
print(list(enumerate(nums)))
print(tuple(enumerate(nums)))
print('-------------------------')

str1 = 'hello'
for index, char in enumerate(str1):
    print(index, char)
print('-------------------------')

colors = ('red', 'green', 'blue')
print(dict(enumerate(colors, start=100)))
print('-------------------------')

students = ['Alice', 'Bob', 'Charlie']
score_dict = {name: score for score, name in enumerate(students, start=90)}
print(score_dict)