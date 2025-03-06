class Person:

    def __init__(self, name, age):
        print("Person的init调用了")
        self.name = name
        self.__age = age

    def say_name(self):
        print("{0}的姓名是{1}".format(self.name, self.name))

    def say_age(self):
        print("{0}的年龄是{1}".format(self.name, self.__age))


class Student(Person):

    def __init__(self, name, age, score):
        # Person.__init__(self, name, age)
        super(Student, self).__init__(name, age)
        print("Student的init调用了")
        self.score = score

    def say_score(self):
        print("{0}的分数是{1}".format(self.name, self.score))

    def say_name(self):
        print("学生--{0}的姓名是{1}".format(self.name, self.name))



s1 = Student("bt", 18, 99)
s1.say_age()
s1.say_score()
s1.say_name()
print(Student.mro())
