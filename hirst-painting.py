# import colorgram
#
# colors = colorgram.extract('dotpainting.jpg', 15)
# color_bank = []
#
# for dict in colors:
#     rgb = dict.rgb
#
#     red = rgb.r
#     green = rgb.g
#     blue = rgb.b
#
#     color = (red, blue, green)
#
#     color_bank.append(color)
#
# print(color_bank)

color_bank = [(247, 234, 242), (237, 248, 242), (249, 244, 240), (239, 244, 247), (139, 195, 168), (206, 121, 154), (192, 150, 140), (25, 55, 36), (58, 140, 105), (145, 162, 178), (151, 58, 68), (137, 76, 68), (229, 107, 212), (47, 41, 36), (145, 36, 29)]


import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

t = Turtle()
t.shape("classic")
t.speed("slow")
t.hideturtle()
t.up()

x_origin = -200
y_origin = -200

t.sety(y_origin)
t.setx(x_origin)

for y in range (1,11):
    t.setx(x_origin)
    for x in range (10):
        t.dot(20, (random.choice(color_bank)))
        t.fd(50)
    new_y = y_origin + y*50
    t.sety(new_y)


screen = Screen()
screen.exitonclick()
