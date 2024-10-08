from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as score:
            self.high_score = int(score.read())
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.high_score}", move=False, align= ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score+=1

        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as data:
                data.write(str(self.high_score))
        self.update_scoreboard()
        self.score = 0


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over", move=False, align= ALIGNMENT, font=FONT)



