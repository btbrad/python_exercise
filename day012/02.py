class Animal:

    def shout(self):
        print("Animal shout")


class Dog(Animal):

    def shout(self):
        print("dog bark")


class Cat(Animal):

    def __init__(self, color):
        self.color = color

    def shout(self):
        print("cat meow")


def animal_shout(s):
    s.shout()


animal_shout(Dog())
animal_shout(Cat("black"))

c1 = Cat("orange")

print(c1.__dict__)
print(c1.__class__)
print(Cat.__bases__)
print(Cat.mro())
print(Animal.__subclasses__())