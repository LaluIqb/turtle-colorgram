import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.hideturtle()
timmy.speed('fastest')
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = (r, g, b)
    return color


for angle in range (0, 360, 5):
    timmy.color(random_color())
    timmy.setheading(angle)
    timmy.circle(100)


screen = Screen()
screen.exitonclick()