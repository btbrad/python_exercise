"""
    乌龟绘图
    奥运五环
"""
import turtle

turtle.showturtle()
turtle.pensize(10)

turtle.color("blue")
turtle.circle(100)

turtle.penup()
turtle.goto(220, 0)
turtle.pendown()
turtle.color("black")
turtle.circle(100)

turtle.penup()
turtle.goto(440, 0)
turtle.pendown()
turtle.color("red")
turtle.circle(100)

turtle.penup()
turtle.goto(110, -100)
turtle.pendown()
turtle.color("yellow")
turtle.circle(100)

turtle.penup()
turtle.goto(330, -100)
turtle.pendown()
turtle.color("green")
turtle.circle(100)

turtle.done()