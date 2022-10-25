from turtle import Turtle
from scoreboard import Scoreboard

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

score = Scoreboard()


def end_game():
    score.end_game()


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("dark blue")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def reset_player(self):
        if self.ycor() >= FINISH_LINE_Y:
            score.update_score()
            self.goto(STARTING_POSITION)
            return True
        else:
            return False

    def move(self):
        self.forward(MOVE_DISTANCE)
