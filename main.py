import time
from turtle import Screen
from player import Player, STARTING_POSITION, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.title("Turtle Crossing")
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.random_location()
    car_manager.car_move()

    # collision with wall
    for car in car_manager.cars:
        if car.distance(player) < 20:
            score_board.game_over()
            game_is_on = False

    if player.ycor() == FINISH_LINE_Y:
        player.goto(STARTING_POSITION)
        score_board.increase_level()
        car_manager.increase_speed()


screen.exitonclick()
