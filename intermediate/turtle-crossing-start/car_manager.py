from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.patch = []
        self.speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        car = Turtle("square")
        car.shapesize(stretch_len=2)
        car.color(random.choice(COLORS))
        car.penup()
        car.goto(310, random.randint(-250, 250))
        self.patch.append(car)

    def generate_next_patch(self):
        if self.patch[-1].xcor() <= 270:
            self.generate_car()

    def move_cars(self):
        for c in self.patch:
            c.goto(c.xcor() - self.speed, c.ycor())

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
