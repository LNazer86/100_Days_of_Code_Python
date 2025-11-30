from turtle import Turtle
FONT = ("Courier", 20, "normal")
ALIGNMENT = "center"

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update()

    def update(self):
        self.clear()
        self.color("white")
        self.write(f"{self.l_score} : {self.r_score}", align=ALIGNMENT, font=FONT)

    def r_increase_score(self):
        self.r_score += 1
        self.update()

    def l_increase_score(self):
        self.l_score += 1
        self.update()



