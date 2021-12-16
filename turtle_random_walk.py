from turtle import Turtle, Screen, colormode
from random import randint, choice

colormode(255)


def random_color():
    r = randint(0, 255)
    b = randint(0, 255)
    g = randint(0, 255)
    random_color_ = (r, b, g)
    return random_color_


directions = [0, 90, 180, 270]
tim = Turtle()
screen = Screen()
tim.hideturtle()
tim.pensize(10)
tim.speed("fastest")

for _ in range(1000):
    tim.color(random_color())
    tim.forward(20)
    tim.setheading(choice(directions))

screen.exitonclick()

