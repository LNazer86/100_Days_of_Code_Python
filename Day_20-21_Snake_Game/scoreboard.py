from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update()

    def update(self):
        self.clear()
        scoreboard = f"Score: {self.counter}"
        self.color("white")
        self.write(scoreboard, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.counter += 1
        self.update()

    def game_over(self):
        self.color("white")
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)