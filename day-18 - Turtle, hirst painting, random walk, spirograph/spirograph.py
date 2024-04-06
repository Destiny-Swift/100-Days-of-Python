import turtle
from random import randint

tim = turtle.Turtle()

turtle.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    color = (r, g, b)
    return color


screen = turtle.Screen()
screen.bgcolor('black')


def draw_spirograph(spacing):
    tim.speed('fastest')
    tim.hideturtle()
    for _ in range(int(360/spacing) + 1):
        tim.color(random_color())
        tim.circle(142)
        tim.right(spacing)


draw_spirograph(0.5)

screen.exitonclick()
