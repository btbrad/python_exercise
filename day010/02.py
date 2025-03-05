class Student:
    count = 0

    company = "Python dev"

    def __init__(self, name, score):
        self.name = name
        self.score = score
        Student.count += 1

    def say_score(self):
        print(f"{self.name}的分数是：{self.score}")

    @classmethod
    def print_company(cls):
        print(cls.company)

    @staticmethod
    def add(x, y):
        return x + y


print(type(Student))

s1 = Student("bt", 90)
s2 = Student("Brad", 70)

print(Student.count)
Student.print_company()
a = Student.add(1, 2)
print(a)