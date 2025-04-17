class Dog:

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def intro(self):
    print(f'my dog {self.name} is {self.age} years old.')

  def sit(self):
    print(f'{self.name} is now sitting.')