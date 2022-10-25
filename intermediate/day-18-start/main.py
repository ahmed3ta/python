import random
from turtle import Turtle, Screen
import random as r
Screen().colormode(255)
tim = Turtle()
tim.speed(0)
# tim.pensize(15)


def random_color():
    r1 = r.randint(0,255)
    p = r.randint(0,255)
    g = r.randint(0, 255)
    return (r1, p, g)
#
#
# for _ in range(200):
#     tim.pencolor(random_color())
#     tim.forward(20)
#     tim.setheading(r.choice([0, 90, 180, 270]))
#     # r.choice([tim.right(90), tim.left(90), tim.backward(90)])


for i in range(0, 360, 2):
    tim.pencolor(random_color())
    tim.circle(100)
    tim.setheading(i)




# import heroes as h
# print(h.gen())













screen = Screen()
screen.exitonclick()