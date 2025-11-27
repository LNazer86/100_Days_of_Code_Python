import turtle
import random

is_race_on = False
screen = turtle.Screen()
screen.setup(500, 400)
user_guess = screen.textinput(title="Make your bet?", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
position = -100
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230, position)
    position += 40
    all_turtles.append(new_turtle)

if user_guess:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_guess:
                print(f"You won! The {winner_color} turtle is the winner!")
            else:
                print(f"You lost! The {winner_color} turtle is the winner!")

        turtle.forward(random.randint(0,10))

screen.exitonclick()
