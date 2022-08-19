import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarGen:

    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def spawn_car(self):
        car_gen = random.randint(1, 6)
        if car_gen == 1:
            car = Turtle("square")
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            car.goto(280, random.randint(-250, 250))
            car.setheading(180)
            self.cars.append(car)

    def move_car(self):
        for car in self.cars:
            car.fd(self.car_speed)

    def increase_speed(self):
        self.car_speed += 0.5 * MOVE_INCREMENT
