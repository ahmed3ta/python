import time
from turtle import Screen
from player import Player, end_game
from car_manager import CarManager


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player1 = Player()

screen.listen()
screen.onkey(player1.move, "Up")


car_manager = CarManager()
car_manager.generate_car()
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    if player1.reset_player():
        car_manager.increase_speed()
    car_manager.move_cars()
    car_manager.generate_next_patch()
    for car in car_manager.patch:
        if player1.distance(car) <= 25:
            game_is_on = False
            end_game()
    screen.update()

screen.exitonclick()
