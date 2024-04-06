from turtle import Turtle

STARTING_POSITION = (0, -280)


class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.color('white')
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def move_up(self):
        self.sety(self.ycor() + 20)

    def move_down(self):
        self.sety(self.ycor() - 20)

    def move_right(self):
        self.setx(self.xcor() + 20)

    def move_left(self):
        self.setx(self.xcor() - 20)

    def is_at_finish_line(self):
        return self.ycor() >= 290

    def go_to_start(self):
        self.goto(STARTING_POSITION)
