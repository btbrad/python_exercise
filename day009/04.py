class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_age(self):
        print(f"{self.name}的年龄是{self.age}岁")


s1 = Student("张三", 18)
print(s1.name, s1.age)
s1.say_age()