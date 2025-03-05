class Car:

    def __call__(self, *args, **kwargs):
        print("called")

    pass

c = Car()
c()