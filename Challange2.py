from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("arrow")
timmy.color('cyan')
timmy.speed('slowest')
timmy.width(2)
timmy.penup()
timmy.setx(-200)

for i in range (15):
    timmy.up()
    timmy.fd(10)
    timmy.down()
    timmy.fd(10)

print(timmy.xcor())
screen = Screen()
screen.exitonclick()
