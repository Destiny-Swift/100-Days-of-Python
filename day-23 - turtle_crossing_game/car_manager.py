from turtle import Turtle
import random

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
STARTING_MOVE_DISTANCE = 2
MOVE_INCREMENT = 2
STARTING_PROBABILITY = 20


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.car_probability = STARTING_PROBABILITY

        self.create_car()

        self.buffer()

    def create_car(self):
        new_car = Turtle('square')
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.setheading(180)
        new_car.shapesize(stretch_len=2, stretch_wid=1)

        random_y = random.randint(-250, 250)  # some organization around here
        while random_y % 20 != 0:
            random_y = random.randint(-250, 250)

        print(f'Random_y: {random_y}')

        new_car.goto(320, random_y)

        self.cars.append(new_car)

    def new_cars(self):
        if random.randint(1, self.car_probability) == 1:
            self.create_car()

    def move_cars(self):
        for car in self.cars:
            if car.xcor() < -330:
                self.cars.remove(car)
            car.forward(self.car_speed)

    def buffer(self):
        while self.cars[0].xcor() > -280:
            self.new_cars()
            self.move_cars()

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

        if self.car_probability > 1:
            self.car_probability -= 1
