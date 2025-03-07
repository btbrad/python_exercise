class Audi: pass
class Auto: pass
class Alpine: pass


class CarFactory:

    def create_car(self, brand):
        if brand == "audi":
            return Audi()
        elif brand == "auto":
            return Auto()
        elif brand == "alpine":
            return Alpine()
        else:
            print("unknown brand")


factory = CarFactory()
car1 = factory.create_car("audi")
car2 = factory.create_car("alpine")

print(car1)
print(car2)