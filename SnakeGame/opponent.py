import random
from turtle import Turtle
DISTANCE = 20
positions = [(270, 270), (-250, 0), (-230, 0)]


class Opponent:
    def __init__(self):
        self.segments = []
        self.directions = [0, 90, 180, 270]
        for i in positions:
            new_turtle = Turtle(shape='square')
            new_turtle.color('white')
            new_turtle.penup()
            new_turtle.goto(i)
            self.segments.append(new_turtle)
        self.head = self.segments[0]

    def move(self):
        for segnum in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segnum - 1].xcor()
            new_y = self.segments[segnum - 1].ycor()
            self.segments[segnum].goto(new_x, new_y)
        if
        self.segments[0].forward(DISTANCE)


