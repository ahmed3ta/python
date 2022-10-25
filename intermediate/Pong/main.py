import time
from turtle import Screen,Turtle
from paddle import Paddle
from seperation import SeparationLine
from ball import Ball
from score_board import Scoreboard

screen = Screen()
screen.title("Pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

# Separation line from the seperation class
separation_mode = SeparationLine()

# Paddles
right_paddle = Paddle(350)
left_paddle = Paddle(-350)

# Paddle Movement
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

# Ball
ball = Ball()

# Scoreboard
score_board = Scoreboard()
game_is_on = True
# ball.reset_position()


while game_is_on:
    ball.move()
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()
    if right_paddle.distance(ball) <= 20 or left_paddle.distance(ball) <= 20:
        ball.bounce_x()
    if ball.xcor() >= 400:
        ball.reset_position()
        score_board.l_point()
    if ball.xcor() <= -400:
        ball.reset_position()
        score_board.r_point()

    screen.update()
    time.sleep(ball.move_speed)
screen.exitonclick()
