from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor('black')

tim = Turtle()
tim.hideturtle()
tim.color('white')
tim.speed('fastest')


# drawing a square
def square(length):
    for i in range(1000):
        tim.forward(length)
        tim.right(71)
        length += 1


square(1)


# drawing a dashed line
# def dash(length):
#     for _ in range(15):
#         tim.forward(length)
#         tim.penup()
#         tim.forward(length)
#         tim.pendown()
#
#
# dash(10)


# # shape madness
# def shapes(length):
#     # square
#     tim.color(random.choice(['red', 'green', 'orange', 'blue', 'violet']))
#     for _ in range(4):
#         tim.forward(length)
#         tim.right(90)
#
#     tim.color(random.choice(['red', 'green', 'orange', 'blue', 'violet']))
#     # pentagon
#     for _ in range(5):
#         tim.forward(length)
#         tim.right(72)
#
#     tim.color(random.choice(['red', 'green', 'orange', 'blue', 'violet']))
#     # hexagon
#     for _ in range(6):
#         tim.forward(length)
#         tim.right(60)
#
#     tim.color(random.choice(['red', 'green', 'orange', 'blue', 'violet']))
#     # heptagon
#     for _ in range(7):
#         tim.forward(length)
#         tim.right(360/7)
#
#     tim.color(random.choice(['red', 'green', 'orange', 'blue', 'violet']))
#     # octagon
#     for _ in range(8):
#         tim.forward(length)
#         tim.right(45)
#
#     tim.color(random.choice(['red', 'green', 'orange', 'blue', 'violet']))
#     # nonagon
#     for _ in range(9):
#         tim.forward(length)
#         tim.right(40)
#
#     tim.color(random.choice(['red', 'green', 'orange', 'blue', 'violet']))
#     # decagon
#     for _ in range(10):
#         tim.forward(length)
#         tim.right(36)
#
#
# shapes(100)


# smarter method
def shapes_madness(length, shape_sides):
    tim.penup()
    tim.goto(x=-(length/2), y=(tim.screen.window_height()/2) - 5)
    tim.pendown()
    tim.speed('fastest')

    for n_side in shape_sides:
        angle = 360 / n_side
        print(f'Side: {n_side}, Angle: {angle}')
        tim.color(random.choice(['red', 'green', 'orange', 'blue', 'violet']))
        for _ in range(n_side):
            tim.forward(length)
            tim.right(angle)


shapes_madness(10, [_ for _ in range(3, 9999999)])


screen.exitonclick()
