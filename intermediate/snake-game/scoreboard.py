from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Verdana', 15, 'bold')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score_count = 0
        with open("data.txt") as data_file:
            high_score_str = data_file.read()
        self.high_score = int(high_score_str)
        self.penup()
        self.clear()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score_count} High score = {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score_count += 1
        self.update_scoreboard()

    def reset(self):
        if self.score_count > self.high_score:
            self.high_score = self.score_count
            high_score_str = str(self.high_score)
            with open("data.txt", mode="w") as data_file:
                data_file.write(high_score_str)

        self.score_count = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over!", align=ALIGNMENT, font=FONT)

# screen = Screen(0)
# screen.screensize(600, 600)
# score = Score()
#
# screen.exitonclick()
