class Employee1:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 0 < age < 130:
            self.__age = age
        else:
            print("年龄录入错误！")


e1 = Employee1("bt", 20)
e1.age = 30
print(e1.age)