from turtle import Turtle


class SeparationLine:
    def __init__(self):
        separation_line = Turtle()
        separation_line.color("white")
        separation_line.hideturtle()
        for sep in range(300, -350, -40):
            separation_line.penup()
            separation_line.goto(0, sep)
            separation_line.pendown()
            separation_line.goto(0, sep+20)


