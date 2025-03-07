class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Person的init")

    def say_age(self):
        print(f"Person类的方法：{self.age}")


class Student(Person):

    def __init__(self, name, age, score):
        super(Student, self).__init__(name, age)
        self.score = score
        print("Student的init")

    def say_age(self):
        super().say_age()
        print(f"Student的方法{self.age}")


s1 = Student('bt', 18, 90)
s1.say_age()

