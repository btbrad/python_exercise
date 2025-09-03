print(isinstance(10, int))
print(isinstance('hello', str))
print(isinstance([1, 2], list))
print(isinstance(3.14, int))
print('-------------------------')
print(isinstance(3.14, (int, float)))
print(isinstance('hello', (int, float)))
print('-------------------------')
class Animal: pass
class Dog(Animal): pass

d = Dog()
print(isinstance(d, Dog))
print(isinstance(d, Animal))
print('-------------------------')
def process(value):
    if isinstance(value, (int, float)):
        return value * 2
    raise TypeError('仅支持数字类型')

print(process(3.14))
# print(process('hi')) # TypeError: 仅支持数字类型