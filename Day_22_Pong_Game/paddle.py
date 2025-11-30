from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)  # turtle začíná 20x20, shapesize nastavuje násobky
        self.showturtle()
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

