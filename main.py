import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=500)
screen.tracer(0)
new_player = Player()
cars = []
for n in range(1, 10):
    car = CarManager()
    cars.append(car)


screen.listen()
screen.onkey(new_player.move, 'Up')


game_is_on = True
while game_is_on:
    for i in cars:
        i.move_car()
    time.sleep(0.1)
    screen.update()

