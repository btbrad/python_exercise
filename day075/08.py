class Student:
    
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def study(self, course_name):
        print(f'{self.name} 正在学习 {course_name}')

    def play(self):
        print(f'{self.name} 正在玩耍')

    def showAge(self):
        print(f'{self.name} 的年龄是：{self.__age}')

    def __repr__(self):
        return f'姓名：{self.name}, 年龄：{self.__age}'


if __name__ == '__main__':
    stu1 = Student('小王', 18)
    stu2 = Student('小李', 17)

    print(stu1)
    print(stu2)

    stu1.study('Python')
    stu2.play()

    stu1.showAge()
    # print(stu1.__age)
    