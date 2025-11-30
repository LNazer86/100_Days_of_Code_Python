from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Score()

screen.listen()
screen.onkey(right_paddle.move_up, "Up") # funkce jako parametr je vždy bez závorek
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

def game_loop():
    screen.update()
    ball.move()


    # detekce kolize mezi míčkem a spodní nebo vrchní linkou
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detekce kolize s pádly
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 330) or (ball.distance(left_paddle) < 50 and ball.xcor() < -330):
        ball.bounce_x()
        ball.increase_speed()


    # detekce promáchnutí
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_increase_score()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_increase_score()

    screen.ontimer(game_loop, 30)


game_loop()
screen.mainloop()

