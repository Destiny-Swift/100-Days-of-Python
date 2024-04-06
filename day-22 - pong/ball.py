from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.speed('fastest')
        self.penup()

        self.x_increase = 10
        self.y_increase = 10

        self.move_speed = 0.1

    def move(self):

        new_x = self.xcor() + self.x_increase
        new_y = self.ycor() + self.y_increase

        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_increase *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_increase *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1
