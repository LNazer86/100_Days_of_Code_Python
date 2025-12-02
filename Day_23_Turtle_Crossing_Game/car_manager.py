from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(1, 6) == 6: # auto se vytvoří jen při 6 - hustota provozu
            car = Turtle("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(1, 2)
            car.setheading(180)
            car.goto(320, random.randint(-260, 260))
            self.cars.append(car)

    def move(self):
        for car in self.cars[:]:
            car.forward(self.car_speed)

            if car.xcor() < -320:
                car.hideturtle()
                self.cars.remove(car)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT





