import turtle as t
from random import randint, choice
import colorgram

colors = [color.rgb for color in colorgram.extract('image.jpg', 10)]
# print(colors)

t.colormode(255)

screen = t.Screen()
screen.bgcolor('black')


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    color = (r, g, b)
    return color


tim = t.Turtle()

tim.penup()
tim.goto(x=-500, y=-300)


tim.pensize(15)
tim.hideturtle()
tim.speed('fastest')


def hirst_dot(num_rows, row_spacing, num_dots, dot_spacing):
    x_origin = tim.xcor()
    y_origin = tim.ycor()
    for _ in range(num_rows):
        for _ in range(num_dots):
            tim.color(choice(colors))
            tim.dot()
            tim.goto(x=tim.xcor()+dot_spacing, y=tim.ycor())

        tim.goto(x=x_origin, y=y_origin + row_spacing)
        y_origin += row_spacing


hirst_dot(num_rows=10, row_spacing=60, num_dots=10, dot_spacing=60)

screen.mainloop()  # keep it running forever....
