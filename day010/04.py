class Person:
    def work(self):
        print("work")

def walk(self):
    print("walk")

Person.walk = walk

p = Person()
p.work()
p.walk()