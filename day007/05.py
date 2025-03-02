import turtle
import random

colors = ("red", "green", "yellow", "blue", "black")
p = turtle.Pen()
p.width(4)

for x in range(10):
    radius = x * 20
    p.penup()
    p.goto(0, -radius)
    p.pendown()
    p.color(colors[random.randint(0,4)])
    p.circle(radius)

turtle.done()