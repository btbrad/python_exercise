d = {'name': 'bt', 'age': 20}

print(d.keys())
print(d.keys().mapping)

keys = ['name', 'age', 'gender']
value = ['bt', 20, 'male']

d2 = dict(zip(keys, value, strict=True))
print(d2)

d3 = {'name': 'bt', 'age': 20, 'job': 'coder'}
d4 = { 'name': 'zs', 'score': 90 }

print(d3 | d4)
d3 |= d4
print(d3)