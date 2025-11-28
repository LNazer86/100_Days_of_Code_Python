from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update() # obnovení obrazovky při Tracer 0
    time.sleep(0.1)
    snake.move()

    # Detekce kolize mezi hadem a potravou
    if (snake.head.distance(food) < 15): # kdyz je vzdalenost mezi food a hadem mensi nez 15px
        score.increase_score()
        food.refresh()
        snake.extend_snake()

    # Detekce mezi hadem a stěnou
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()

    # Detekce kolize mezi hadem a jeho ocasem
    for segment in snake.segments[1:]: # musíme vynechat hlavu hada - 1. segment
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
