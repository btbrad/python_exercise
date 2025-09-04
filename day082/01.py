nums = [5, 2, 9, 1]
print(sorted(nums))
print(sorted(nums, reverse=True))
print('-------------------------')

str1 = 'hello'
print(sorted(str1))
print('-------------------------')

dict1 = {'c': 3, 'a': 1, 'b': 2}
print(sorted(dict1))
print(sorted(dict1.values()))
print('-------------------------')

words = ['banana', 'apple', 'pear', 'grape']
print(sorted(words))
print(sorted(words, key=len))
print('-------------------------')

scores = [{'name': 'Alice', 'score': 88}, {'name': 'Bob', 'score': 95}, {'name': 'Charlie', 'score': 78}]
print(sorted(scores, key=lambda x: x['score'], reverse=True))