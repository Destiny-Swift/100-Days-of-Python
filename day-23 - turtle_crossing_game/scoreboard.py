from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.penup()
        self.color('white')

        self.level = 1

        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(-230, 260)
        self.write(f'Level: {self.level}', align='center', font=('Press Start 2P', 10, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=('Press Start 2P', 40, 'normal'))
