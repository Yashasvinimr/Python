from turtle import Turtle, Screen
import random
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
screen = Screen()
screen.setup(500, 400)
choice = screen.textinput("Mke your bet", "Which turtle will win the race? Choose a color:")
y_position =[-70, -40, -10, 20, 50, 80]
rate = ['slow', 'slowest', 'normal', 'fast', 'fastest']
all_turtle = []
for i in range(6):
    new_turtle = Turtle(shape='turtle')
    all_turtle.append(new_turtle)
    new_turtle.penup()
    current_y = new_turtle.position()
    new_turtle.goto(x=-230, y=y_position[i])
    new_turtle.color(colors[i])

is_race_on = False
if choice:
    is_race_on = True
while is_race_on:

    for turtles in all_turtle:
        dist = random.randint(0, 10)

        if turtles.xcor()>230:
            is_race_on=False
            winner = turtles.pencolor()
            if turtles.pencolor()=='choice':
                print(f"You won! The winner is {winner}.")
            else:

                print(f"You lose! The winner is {winner}. ")
        else:
            turtles.forward(dist)



screen.exitonclick()