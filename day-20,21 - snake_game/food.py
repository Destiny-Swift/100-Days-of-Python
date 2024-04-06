from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('yellow')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed('fastest')

        self.refresh()

    def refresh(self):
        # go to random position on screen
        def get_random_position():
            rand_x = randint(-280, 280)
            while rand_x % 20 != 0:
                rand_x = randint(-280, 280)

            rand_y = randint(-280, 220)
            while rand_y % 20 != 0:
                rand_y = randint(-280, 220)
            return rand_x, rand_y

        random_x = get_random_position()[0]
        random_y = get_random_position()[1]

        # all the lines of code above so the food wouldn't appear on the scoreboard 😑
        # This isn't the best tol for building a snake game.

        # the above tactic is to make sure the food is aligned with the center of the snake head

        self.goto(random_x, random_y)
