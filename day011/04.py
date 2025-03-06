class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        print("重写str")
        return "姓名是{0}，年龄是{1}".format(self.name, self.age)


p1 = Person("bt", 18)

print(p1)
print(str(p1))
