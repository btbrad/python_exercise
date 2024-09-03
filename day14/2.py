'''
创建狗类，实例化两个对象并调用其函数，画出内存图。
数据：品种、昵称、身长、体重
行为：吃(体重增长1)
'''

class Dog:
    def __init__(self, breed, nickname, length, weight):
        self.breed = breed
        self.nickname = nickname
        self.length = length
        self.weight = weight

    def eat(self):
        self.weight += 1

shepard = Dog('shepard', 'haha', 150, 50)
husky = Dog('husky', 'lala', 120, 70)

shepard.eat()
print(shepard.weight)

husky.eat()
print(husky.weight)