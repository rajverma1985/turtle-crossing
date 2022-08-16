import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(.80, 1.5)
        self.penup()
        self.color(random.choice(COLORS))
        self.spawn_car()

    def spawn_car(self):
        self.goto(380, random.randint(-240, 240))
        self.setheading(180)

    def move_car(self):
        self.fd(MOVE_INCREMENT)
