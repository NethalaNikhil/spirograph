import random
import turtle
from turtle import Screen, Turtle
import random

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    r_color = (r, g, b)
    return r_color


screen = Screen()
tim = Turtle()
k = 0
tim.speed("fastest")


def draw(gap):
    for i in range(int(360/gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap)


draw(5)
screen.exitonclick()
