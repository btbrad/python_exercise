import types


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    p1 = Person('p1', 20)
    p2 = Person('p2', 18)

    p1.score = 90
    print(p1.score)

    def run(self):
        print(f'{self.name} is running...')

    p1.run = types.MethodType(run, p1)
    p1.run()