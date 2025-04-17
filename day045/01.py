from dog import Dog

class Husky(Dog):
  def __init__(self, name, age, color):
    super().__init__(name, age)
    self.color = color

  def show_color(self):
    print(f'{self.name} is {self.color} color.')

  def sit(self):
    print(f'{self.name} is now sitting and being silly.')

h = Husky('Kobe', 2, 'brown')
h.sit()
h.show_color()
h.intro()        
