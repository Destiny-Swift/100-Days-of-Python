from turtle import Screen
from scoreboard import Scoreboard
from player import Player
from car_manager import CarManager
import time


screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

godspeed_toggle = 0


def godspeed():  # 😈😈😈😈
    global godspeed_toggle
    if godspeed_toggle == 0:
        godspeed_toggle = 1
    else:
        godspeed_toggle = 0


def teleport():  # 😈😈😈😈😈
    player.sety(280)


screen.onkeypress(player.move_up, 'Up')
screen.onkeypress(player.move_down, 'Down')
screen.onkeypress(player.move_right, 'Right')
screen.onkeypress(player.move_left, 'Left')
screen.onkeypress(godspeed, 'BackSpace')
screen.onkey(teleport, 'T')


game_is_on = True
while game_is_on:
    time.sleep(0.0001)  # fast refresh rate to increase button control response
    screen.update()

    if godspeed_toggle == 0:
        car_manager.new_cars()
        car_manager.move_cars()
        player.color('white')
    else:
        player.color('red')  # some dramatic effect

    # Refresh scoreboard
    scoreboard.refresh()

    # Detect collision with car
    for car in car_manager.cars:
        if car.distance(player) < 30:
            if player.ycor() == car.ycor():
                game_is_on = False
                scoreboard.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.level += 1

    print(player.ycor(), car_manager.car_probability)

screen.exitonclick()
