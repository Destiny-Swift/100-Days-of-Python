from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

WALLS = 1  # variable to determine border walls
IMMORTALITY = 0  # variable to determine immortality 😏😈

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

barrier = Turtle('square')
barrier.color('white')
barrier.shapesize(stretch_len=30, stretch_wid=0.1)
barrier.penup()
barrier.goto(0, 251)

left_barrier = Turtle('square')
left_barrier.color('white')
left_barrier.shapesize(stretch_wid=40, stretch_len=1)
left_barrier.penup()
left_barrier.setx(-305)
left_barrier.sety(-150)
# left_barrier.hideturtle()

# pause functionality
pause = 0


def pause_game():
    global pause
    if pause == 0:
        pause = 1
    else:
        pause = 0


def immortality():
    global IMMORTALITY
    if IMMORTALITY == 1:
        IMMORTALITY = 0
    else:
        IMMORTALITY = 1


abundance = 0


def abundance_toggle():
    global abundance
    if abundance == 1:
        abundance = 0
    else:
        abundance = 1


def activate_abundance():
    if snake.head.heading() == 0:
        food.setposition(snake.head.xcor() + 20, snake.head.ycor())
    elif snake.head.heading() == 180:
        food.setposition(snake.head.xcor() - 20, snake.head.ycor())
    elif snake.head.heading() == 90:
        food.setposition(snake.head.xcor(), snake.head.ycor() + 20)
    elif snake.head.heading() == 270:
        food.setposition(snake.head.xcor(), snake.head.ycor() - 20)

    # deal with food not appearing on screen
    if food.xcor() > 280:
        food.setx(-260)
    elif food.xcor() < -280:
        food.setx(260)
    elif food.ycor() > 220:
        food.sety(-260)
    elif food.ycor() < -280:
        food.sety(220)


def walls():
    global WALLS
    if WALLS == 1:
        WALLS = 0
    else:
        WALLS = 1


# event listeners to control the snake
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')
screen.onkey(pause_game, 'BackSpace')
screen.onkey(immortality, '1')
screen.onkey(walls, '2')
screen.onkey(abundance_toggle, 'f')


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    if pause == 0:
        # move the snake forward
        snake.move()
        scoreboard.refresh(IMMORTALITY, WALLS, abundance)  # Update scoreboard()
    else:
        scoreboard.pause()  # the pause text after refresh so it's visible

    # Detect collision with food
    if snake.head.distance(food) < 15:
        if abundance == 0:
            food.refresh()  # change food position on screen
        elif abundance == 1:
            activate_abundance()
        snake.extend()  # extend snake length
        scoreboard.score += 1

    # walls
    if WALLS == 0:
        if snake.head.xcor() > 280 and snake.segments[1].xcor() < snake.head.xcor():  # additional code to fix soe bug
            snake.head.setx(-280)
        elif snake.head.xcor() < -280:
            snake.head.setx(280)
        elif snake.head.ycor() > 240:
            snake.head.sety(-280)
        elif snake.head.ycor() < -280:
            snake.head.sety(240)
    else:
        # Detect collision with wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 240 or snake.head.ycor() < -290:
            snake.reset()
            scoreboard.reset()
            print('Killed by Wall')

    # immortality
    if IMMORTALITY == 1:
        pass
    else:
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:  # best value to escape the segments position drift glitch
                print(snake.head.distance(segment))
                snake.reset()
                scoreboard.reset()

    # some functionality that makes the product more perfect and the experience more awesome
    scoreboard.update()  # update different from refresh

screen.exitonclick()


# Seems that we're back in the glitch paradox that made me rebuild the whole thing from scratch and I could tell you one
# thing - it ain't funny at all. Trying to solve these glitches and bugs, and so I'd have a perfect game has been the
# source of my impediments, and it ain't funny at all, not one bit.
# Case 1 - the food doesn't disappear instantaneously, upon impact of the snake head with the food.
# Case 2 - the new segment appears in the middle of the screen, and visibly before going to its right position at the
# end of the snake.
# What is all this?
# And then there's Case 3 - This fucking conditional statement for detecting collision with food prevents the snake from
# eating the food after sometime
# if snake.head.xcor() == food.xcor() or snake.head.ycor() == food

# Solving Case 1 gives birth to Case 2. So a way to align the new segment properly, independent of the move function of
# the snake.
# Should also figure out how to do a python multi-line comment.

# Solving Case  without giving birth to Case 2 was as simple as moving the new segment to the position of the last
# and then letting it extend out when next the snake moves.
# This is a solution that doesn't give birth to Case 2 of food not disappearing instantaneously due to the fact the food
# refresh runs whn the snake head is already under the food.
# food.refresh() would run with the next move() not the intended one
# Takes some physical visualizations or goD-level intellect brain power.

# Thanks to my best friend print(), I was able to do some visualizations and find out that Case 3 is due to the glitch
# in the module and is in no way my fault.

# Snake Game done and dusted
# Conclusion - this ain't the best tool to build a snake game. Thank God for my goD-level intellect.
