from turtle import Turtle, Screen, colormode
from random import randint

colormode(255)


def random_color():
    r = randint(0, 255)
    b = randint(0, 255)
    g = randint(0, 255)
    random_c = (r, b, g)
    return random_c


tim = Turtle()
screen = Screen()
tim.speed(0)

for _ in range(360//5):
    tim.color(random_color())
    tim.circle(radius=200)
    tim.left(5)


screen.exitonclick()
