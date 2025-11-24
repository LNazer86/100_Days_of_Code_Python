import turtle
import random

color_list = [(131, 164, 204), (228, 149, 99), (30, 44, 64), (166, 58, 48), (202, 135, 147), (237, 212, 85), (41, 101, 150), (135, 183, 161), (150, 62, 71), (52, 42, 45), (159, 33, 31), (219, 82, 73), (238, 165, 155), (58, 117, 99), (60, 49, 45), (173, 29, 31), (231, 163, 168), (35, 61, 56), (15, 96, 71), (33, 60, 107), (170, 188, 222), (188, 101, 111), (104, 126, 161), (14, 85, 109), (174, 200, 188), (33, 151, 211)]

dot = turtle.Turtle()
dot.speed("fastest")
turtle.colormode(255)
screen = turtle.Screen()

dot.penup()
dot.hideturtle()
dot.goto(-250, -250)

for x in range(10):
    for y in range(10):
        random_color = random.choice(color_list)
        dot.fillcolor(random_color)
        dot.begin_fill()
        dot.circle(10)
        dot.end_fill()
        dot.forward(50)
    dot.backward(10 * 50)
    dot.left(90)
    dot.forward(50)
    dot.right(90)

screen.exitonclick()