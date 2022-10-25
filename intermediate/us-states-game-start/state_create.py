from turtle import Turtle


class StateCoorCreate(Turtle):
    def __init__(self, x, y, state_name):
        super().__init__()
        self.penup()

        self.goto(x,y)
        self.write(state_name, align="center", font=("Courier", 10, "bold"))
        self.hideturtle()
