class Student:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def say_score(self):
        print(f"{self.name}的成绩是: {self.score}")


s1 = Student("bt", 100)
s1.say_score()
# print(s1.age) #报错

s2 = Student("Brad", 98)
s2.age = 16
print(s2.age)

print(dir(s1))
print(s1.__dict__)
print(isinstance(s1, Student))