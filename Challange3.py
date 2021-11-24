from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("arrow")
timmy.color('cyan')
timmy.speed('slow')
timmy.width(2)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def draw_shape(n_side):
    deg = 360/n_side

    for draw_side_n in range (n_side):
        timmy.fd(100)
        timmy.right(deg)


for shape in range (3,11):
    timmy.color(random.choice(colours))
    draw_shape(shape)


screen = Screen()
screen.exitonclick()
