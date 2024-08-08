import time
from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
# from opponent import Opponent
import random
screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)
score = Scoreboard()
snake = Snake()
# oppo = Opponent()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    time.sleep(0.1)
    # oppo.move()
    # oppo.head.setheading(random.choice(oppo.directions))
    # oppo.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.increase()
        score.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        snake.reset()
        score.reset()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()
    # for segment in oppo.segments:
    #     if snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         score.reser()
    # segments[0].left(90)

screen.exitonclick()
