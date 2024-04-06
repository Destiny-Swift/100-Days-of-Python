from turtle import Turtle

ALIGN = 'center'
FONT = ('Courier', 16, 'normal')
FONT2 = ('Courier', 8, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0

        with open('data.txt') as file:
            self.high_score = int(file.read())

        # modify objects
        self.hideturtle()
        self.penup()
        self.pencolor('white')

        # set position
        self.goto(0, 270)

        # initial print
        # self.refresh(0, 0, 0)

    def refresh(self, immortality, walls, abundance):
        self.clear()
        self.goto(0, 270)
        self.write(f'Score: {self.score} High Score: {self.high_score}', align=ALIGN, font=FONT)
        self.goto(-220, 255)
        self.write(f'Immortality: {immortality} \nWalls:\t{walls} \nAbundance: {abundance}', align=ALIGN, font=FONT2)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGN, font=('Courier', 28, 'normal'))

    def pause(self):
        self.goto(0, 0)
        self.write('PAUSE', align=ALIGN, font=('Courier', 28, 'normal'))

    def reset(self):
        self.update()
        self.score = 0
        self.refresh(0, 0, 0)  # arguments would get replaced by actual values; line could more or less be deleted

    def update(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(f'{self.high_score}')
