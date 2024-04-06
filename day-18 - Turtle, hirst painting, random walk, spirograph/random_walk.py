from turtle import Turtle, Screen, colormode
from random import choice, randint

colormode(255)  # read about this, allows you to use rgb


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    color = (r, g, b)
    return color


screen = Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor('black')

tim = Turtle()
tom = Turtle()

tom.speed('fastest')
tim.hideturtle()
tom.pensize(10)

tim.speed('fastest')
tim.pensize(10)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

for _ in range(2000):
    tim.color(random_color())
    tim.forward(30)
    tim.right(choice([0, 90, 180, 270]))
    if tim.xcor() >= screen.window_width()/2 or tim.xcor() <= -(screen.window_width()/2):
        tim.penup()
        tim.home()
        tim.pendown()
    if tim.ycor() >= screen.window_height()/2 or tim.ycor() <= -(screen.window_height()/2):
        tim.penup()
        tim.home()
        tim.pendown()

    # tom.color('black')
    # tom.forward(30)
    # tom.right(choice([0, 90, 180, 270]))
    # if tom.xcor() >= screen.window_width()/2 or tom.xcor() <= -(screen.window_width()/2):
    #     tom.penup()
    #     tom.home()
    #     tom.pendown()
    # if tom.ycor() >= screen.window_height()/2 or tom.ycor() <= -(screen.window_height()/2):
    #     tom.penup()
    #     tom.home()
    #     tom.pendown()
screen.exitonclick()
