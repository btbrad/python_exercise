class Person:

  def __init__(self, name):
    self.name = name

  def greet(self):
    return f'Hello, my name is {self.name}'


p = Person('Alice')
print(getattr(p, 'name'))  # Alice
print(getattr(p, 'age', 18))  # 18
print('-------------------------')
print(hasattr(p, 'greet'))  # True
print(hasattr(p, 'age'))  # False
print(hasattr(p, 'name'))  # True
print('-------------------------')
setattr(p, 'age', 30)
print(p.age)  # 30
print('-------------------------')
def from_dict(obj, attr_dict):
  for key, value in attr_dict.items():
    setattr(obj, key, value)

attr_dict = {'country': 'USA', 'job': 'Engineer', 'married': False}
from_dict(p, attr_dict)
print(p.country)  # USA
print(p.job)
print(p.married)  # False
print('-------------------------')    