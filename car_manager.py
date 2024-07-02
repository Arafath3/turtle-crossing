from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.random_location()
        self.move_speed = 0.1

    def random_location(self):
        random_choice = random.randint(1, 6)
        if random_choice == 1:
            random_y = random.randint(-220, 220)
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            car.setheading(180)
            car.goto(300, random_y)
            self.cars.append(car)

    def car_move(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)


    def increase_speed(self):
        self.move_speed *= .9
