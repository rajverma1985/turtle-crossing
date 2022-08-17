import random
import time
from turtle import Screen
from player import Player
from car_manager import CarGen
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
new_player = Player()
car = CarGen()

screen.listen()
screen.onkey(new_player.move_up, 'Up')


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.spawn_car()
    car.move_car()



