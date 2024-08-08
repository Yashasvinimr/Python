from turtle import Turtle
MOVE_Distance = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0,-280)
        self.setheading(90)

    def move(self):
        if self.ycor()<= 270:
            self.forward(MOVE_Distance)

    def is_at_finish_line(self):
        if self.ycor()==270:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(0,-280)


