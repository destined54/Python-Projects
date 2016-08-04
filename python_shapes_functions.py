from turtle import *
penup()
back(250)
pendown()
def draw(number_sides):
    for i in range(number_sides):
        forward(75)
        right(360/number_sides)
    penup()
    forward(300)
    pendown()

draw(6)

