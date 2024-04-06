from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

FONT = ('Press Start 2P', 20, 'bold')

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.listen()
screen.tracer(0)


right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
net = Turtle()

net.color('white')
net.hideturtle()
net.penup()
net.goto(0, -335)
net.write("""|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n""", align='center', font=FONT)


right_distance = 61
left_distance = 61

pause = 0


def pause_game():
    global pause
    if pause == 0:
        pause = 1
    else:
        pause = 0


def right_cheat():  # 😈😈😈😈
    global right_distance
    right_distance = 450
    right_paddle.shapesize(stretch_len=1, stretch_wid=65)


def left_cheat():
    global left_distance
    left_distance = 450
    left_paddle.shapesize(stretch_len=1, stretch_wid=65)


def right_stop_cheat():  # 😇😇😇😇😇
    global right_distance
    right_distance = 61
    right_paddle.shapesize(stretch_len=1, stretch_wid=5)


def left_stop_cheat():
    global left_distance
    left_distance = 61
    left_paddle.shapesize(stretch_len=1, stretch_wid=5)


screen.onkeypress(right_paddle.up, 'Up')
screen.onkeypress(right_paddle.down, 'Down')
screen.onkeypress(left_paddle.up, 'w')
screen.onkeypress(left_paddle.down, 's')
screen.onkey(right_cheat, ']')
screen.onkeyrelease(right_stop_cheat, '[')
screen.onkey(left_cheat, '1')
screen.onkey(left_stop_cheat, '2')
screen.onkey(pause_game, 'BackSpace')


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    if pause == 0:
        ball.move()

    # Detect collision with top and bottom walls to change ball direction
    if ball.ycor() >= 290 or ball.ycor() <= -280:
        ball.bounce_y()

    # Detect collision with paddles to change ball direction
    if 330 == ball.xcor() < right_paddle.xcor() and ball.distance(right_paddle) < right_distance:
        ball.bounce_x()

    if -330 == ball.xcor() > left_paddle.xcor() and ball.distance(left_paddle) < left_distance:
        ball.bounce_x()

    # Detect when right paddle misses the ball
    if ball.xcor() >= 390:
        ball.reset_position()
        scoreboard.l_point()

    # Detect when left paddle misses the ball
    if ball.xcor() <= -395:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
