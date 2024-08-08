from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')


screen.title("My Pong Game")
screen.tracer(0)
r_paddle=Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball=Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor() < -280:
        ball.bounce()

    if ball.xcor()>380:
        ball.reset_ball()
        scoreboard.l_point()

    if ball.xcor()<-380:
        ball.reset_ball()
        scoreboard.r_point()

    if (ball.xcor() > 320 and ball.distance(r_paddle) < 50) or (ball.xcor() < -320 and ball.distance(l_paddle) < 50):
        ball.collision()


screen.exitonclick()