# import colorgram
# from colorgram import extract
# rgb_colors = []
# colors = colorgram.extract('hirstdots.jpg', 30)
# for _ in colors:
#     r = _.rgb.r
#     g = _.rgb.g
#     b = _.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)
import random
import turtle
from turtle import Turtle, Screen
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
turtle.colormode(255)
timmy_the_turtle.speed("fastest")
timmy_the_turtle.hideturtle()
color_list = [(239, 237, 233), (235, 238, 243), (232, 240, 236), (243, 235, 239), (196, 158, 115), (147, 81, 55), (129, 167, 187), (52, 106, 138), (135, 180, 151), (230, 208, 110), (60, 38, 27), (64, 118, 81), (194, 140, 156), (138, 68, 89), (140, 22, 36), (23, 43, 68), (68, 28, 41), (163, 152, 62), (145, 29, 21), (83, 159, 103), (193, 86, 112), (209, 91, 63), (29, 52, 37), (164, 209, 182), (61, 155, 176), (222, 172, 182), (29, 57, 115), (30, 88, 54), (226, 177, 167), (111, 120, 160)]
n = 0
timmy_the_turtle.setheading(225)
timmy_the_turtle.penup()
timmy_the_turtle.forward(300)
timmy_the_turtle.setheading(0)
while n < 10:
    current_position = timmy_the_turtle.position()
    for i in range(10):
        timmy_the_turtle.dot(20)
        timmy_the_turtle.pencolor(random.choice(color_list))
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(50)
    timmy_the_turtle.setposition(current_position[0], current_position[1]+50)
    n += 1


screen = Screen()
screen.exitonclick()