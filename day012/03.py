class CPU:

    def calculate(self):
        print("CPU is calculating...")


class Screen:

    def display(self):
        print("picture is displayed")


class Computer:

    def __init__(self, cpu, screen):
        self.cpu = cpu
        self.screen = screen


cpu1 = CPU()
screen1 = Screen()
c1 = Computer(cpu1, screen1)
c1.cpu.calculate()
c1.screen.display()

