import random
import turtle

screen = turtle.Screen()
screen.setup(width=500, height=400)

# user_bit = screen.textinput(title="Make your bit", prompt="Which Turtle will win the race")

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(x=-220, y=150)
pen.pendown()
pen.setheading(270)
pen.forward(300)

colors = ["red", "blue", "green", "orange", "purple"]

x = 0

all_turtle = []
for i in range(0, 5):
    new_turtle = turtle.Turtle()
    new_turtle.color(colors[i])
    new_turtle.speed(0)
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + x)
    new_turtle.speed("slowest")
    x += 50
    all_turtle.append(new_turtle)

no_win = True
# print(willis.pos())
user_bit = screen.textinput(title="Make your bit", prompt="Which Turtle will win the race")
while no_win:
    for i in all_turtle:
        r = random.randint(1,12)
        i.forward(r)
        if i.pos()[0] >= 250:
            no_win = False


if i.color()[0] == user_bit:
    print(f"Way to go! Turtle {i.color()[0]} Wins")
else:
    print(f"you lose Turtle {i.color()[0]} Wins")




