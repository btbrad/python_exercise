class Employee:

    __company = "Python dev"

    def say_company(self):
        print(f"公司是: {Employee.__company}")

    def __work(self):
        print("work")

print(dir(Employee))
print(Employee._Employee__company)

e = Employee()
e.say_company()
e._Employee__work()