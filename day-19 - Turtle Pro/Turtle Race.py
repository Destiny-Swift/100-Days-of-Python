from turtle import Turtle, Screen
from random import randint
screen = Screen()
width = 500
height = 400
screen.setup(width=width, height=height)
screen.bgcolor('black')

prediction = screen.textinput(title='', prompt='Make your winning prediction:')


colors = ['purple', 'blue', 'green', 'yellow', 'orange', 'red', 'white', 'pink', 'silver', 'gold', 'indigo']
all_turtles = []

step = (height - (60*2))/len(colors)
y_position = -(height/2) + 80

for turtle_index in range(0, len(colors)):  # another astute way of getting stuff done 😎
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.speed('fast')
    new_turtle.goto(x=-(width/2) + 20, y=y_position)
    y_position += step
    all_turtles.append(new_turtle)
    new_turtle.speed('normal')


def nitro():
    for tiny_turtle in all_turtles:
        if tiny_turtle.pencolor() == prediction:
            tiny_turtle.forward(10)


race_is_on = True
while race_is_on:  # which ever turtle gets to 200 first wins
    for turtle in all_turtles:
        turtle.forward(randint(0, 10))

        # a little cheat I just thought about adding
        screen.listen()
        screen.onkeypress(key='space', fun=nitro)

        if turtle.xcor() >= ((width/2) - 30):
            winner = turtle.pencolor()
            print(f'The winner is {winner}')
            if prediction == winner:
                print(f'OMG, you were right!\nCash-out: $1k')
            elif prediction == '' or prediction is None:
                pass
            else:
                print('Idiot🙄')
            race_is_on = False
            break


screen.exitonclick()
