import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 7


# MOVE_INCREMENT = 10

class CarManager(Turtle):
    """class to represent all cars on the screen"""

    def __init__(self):
        super().__init__()
        self.MOVE_INCREMENT = 0
        self.allCars = []  # keeps all cars so that we refer to them later to do some actions
        # like , drive, compare distance with player and more

    def createCar(self):  # creates car
        slower = random.randint(1, 10)  # creates only when the randomly generated number is 1,
                                        # this prevents excess car object generation
        if slower == 1:
            newCar = Turtle()
            newCar.shape('square')
            newCar.shapesize(stretch_wid=1, stretch_len=2)
            newCar.penup()
            newCar.color(random.choice(COLORS))
            randY = random.randrange(-250, 250, 50)
            newCar.goto(300, randY)  # cars generated on y axis on random position,
            self.allCars.append(newCar)  # cars added to list

    def moveCars(self):  # moves car
        for car in self.allCars:
            car.backward(STARTING_MOVE_DISTANCE)  # move 10 unit each time the loop runs,

    def spedUp(self):    # speed up cars whenever user reaches a higher level
        self.MOVE_INCREMENT += 10  # increase the current step by 10
        for car in self.allCars:
            car.backward(self.MOVE_INCREMENT)  # move cars with this step
