FONT = ("Courier", 15, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    """Class to represent the score board"""

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('black')
        self.penup()
        self.goto(-270, 250)
        self.level = "Level"
        self.levelNumber = 1  # initial game level set to 1
        self.write(f"{self.level} : {self.levelNumber}", align='left', font=FONT)  # score board content

    def updateBoard(self):  # updates score board whenever user reaches new level
        self.clear()  # so that it does not write new score on existing one,
        self.levelNumber += 1  # increase level number
        self.write(f"{self.level} : {self.levelNumber}", font=FONT)  # update text

    def gameOver(self):  #
        self.clear()
        self.goto(-20, 0)
        self.write(f"Game Over!", font=('Arial', 20, 'normal'))
