from turtle import Turtle
import random

class Food(Turtle): 

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        #makes size 10x10 pixels so smaller
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("orange")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_xvar = random.randint(-280, 280)
        random_yvar = random.randint(-280, 280)
        self.goto(random_xvar,random_yvar)