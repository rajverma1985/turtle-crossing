import random
import time
from turtle import Screen
from player import Player
from car_manager import CarGen
from scoreboard import Scoreboard, LevelUp

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
new_player = Player()
car = CarGen()
score = Scoreboard()
levels = LevelUp()
screen.listen()
screen.onkey(new_player.move_up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.spawn_car()
    car.move_car()
    for cars in car.cars:
        if new_player.distance(cars) < 20:
            game_is_on = False
            score.game_over()
    if new_player.top():
        new_player.go_to_start()
        score.keep_score()
        levels.level_up()
        car.increase_speed()

screen.exitonclick()
