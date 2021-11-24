import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.hideturtle()
timmy.speed('fastest')
timmy.width(7)
turtle.colormode(255)

angle = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_color = (r, g, b)
    return random_color


for _ in range (200):
    timmy.color(random_color())
    timmy.fd(20)
    timmy.setheading(random.choice(angle))


screen = Screen()
screen.exitonclick()