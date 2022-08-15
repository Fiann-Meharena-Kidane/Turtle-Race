STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle


class Player(Turtle):
    """class to represet the turtle (player)"""
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)    # starts a the bottom centre of the screen
        self.setheading(90)   # head set to North

    def goUp(self):  # moves turtle up when Up key is pressed
        self.forward(MOVE_DISTANCE)

    def isAtFinishLine(self):  # checks if turtle is at finish line,
        if self.ycor() > 280:
            return True
        else:
            return False

    def PositionReset(self):  # places turtle at the bottom centre
        self.goto(STARTING_POSITION)


