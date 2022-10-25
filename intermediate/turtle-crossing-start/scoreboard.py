from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_count = 0
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.write(f"score: {self.score_count}", align="center", font=FONT)

    def update_score(self):
        self.score_count += 1
        self.clear()
        self.write(f"score: {self.score_count}", align="center", font=FONT)

    def end_game(self):
        self.home()
        self.write(f"Game Over", align="center", font=FONT)
