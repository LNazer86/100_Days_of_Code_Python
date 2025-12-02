from turtle import Turtle
FONT = ("Courier", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.current_level = 1

    def show_level(self):
        self.clear()
        self.goto(-270, 260)
        self.write(arg=f"Level: {self.current_level}", font=FONT)

    def level_up(self):
        self.current_level += 1
        self.show_level()

    def game_over(self):
        self.home()
        self.write(arg="Game Over", align="center", font=FONT)

