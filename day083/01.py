names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
countries = ['USA', 'UK', 'Canada']

for name, age, country in zip(names, ages, countries):
    print(f'{name} is {age} years old and comes from {country}.')

print('-------------------------')    

from itertools import zip_longest

numbers = [1, 2, 3, 4, 5]
letters = ['A', 'B', 'C']

for number, letter in zip_longest(numbers, letters, fillvalue='N/A'):
    print(f'Number: {number}, Letter: {letter}')

print('-------------------------')

keys = ['name', 'age', 'country']
values = ['Alice', 25, 'USA']
my_dict = dict(zip(keys, values))
print(my_dict)

print('-------------------------')
zipped_data = [('Alice', 25, 'USA'), ('Bob', 30, 'UK'), ('Charlie', 35, 'Canada')]
names, ages, countries = zip(*zipped_data)
print(f'Names: {names}')