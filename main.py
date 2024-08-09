import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

player = Player()
car = CarManager()
level = Scoreboard()

screen.onkey(player.move, "Up")

game_is_on = True
loop_counter = 0

while game_is_on:
    loop_counter += 1
    time.sleep(0.1)
    screen.update()

    # Make cars generate with every 6th loop
    if loop_counter % 6 == 0:
        car.generate_car()
    car.move()

    # Detect player collision with car
    for a_car in car.all_cars:
        if a_car.distance(player) < 20:
            game_is_on = False
            level.game_over()

    # Detect when player has reached finish line
    if player.ycor() == 280:
        player.reach_finish()
        car.increase_speed()
        level.increase_level()

screen.exitonclick()