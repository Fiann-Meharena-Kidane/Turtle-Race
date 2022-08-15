from turtle import Turtle,Screen
import time
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player=Player()
car_manager=CarManager()
scoreBoard=Scoreboard()

screen.onkey(player.goUp,'Up')

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.createCar()   # create cars on screen
    car_manager.moveCars()   # start moving cars backward at 10 units each time,

    for car in car_manager.allCars:   # for each car in our list,
        if car.distance(player)<30:  # if it collides with player
            scoreBoard.gameOver()   # game over
            game_is_on=False     # quit game

    if player.isAtFinishLine():   # if player finishes one level
        player.PositionReset()   # place player at initial position
        scoreBoard.updateBoard()  # update score and level
        car_manager.spedUp()    # increase speed

screen.exitonclick()