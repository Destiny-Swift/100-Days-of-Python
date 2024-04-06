from turtle import Turtle, Screen


# Little advice from papa when dealing with inbuilt functions and modules; it pays to read documentation and know
# all the shit involved and how they all work.

sketcher = Turtle()

screen = Screen()


def forward():
    sketcher.forward(10)


def backward():
    sketcher.backward(10)


def right():
    sketcher.right(5)


def left():
    sketcher.left(5)


def clear():
    sketcher.reset()


def pen_up():
    sketcher.penup()


def pen_down():
    sketcher.pendown()


def hexagon():
    for sides in range(6):
        sketcher.forward(100)
        sketcher.lt(60)  # lt is an alternative to the left method.


def circle():
    sketcher.circle(100)


screen.listen()


screen.onkeypress(key='Right', fun=right)
screen.onkeypress(key='Left', fun=left)
screen.onkeypress(key='Up', fun=forward)
screen.onkeypress(key='Down', fun=backward)
screen.onkeypress(key='BackSpace', fun=clear)
screen.onkeypress(key='space', fun=pen_up)
screen.onkeyrelease(key='space', fun=pen_down)  # right after pen+up is over; pen_down
screen.onkeypress(hexagon, 'h')
screen.onkey(circle, 'c')

# It's so damn good to be back, I miss python and angela so much, and I'm not abandoning them again - my child and wife.

screen.exitonclick()
