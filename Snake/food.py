
from turtle import Turtle
import random

BOUNDARY = 360


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("HotPink")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed(0)
        self.refresh()

    def refresh(self):
        """Move food to random position"""
        x = random.randint(-BOUNDARY, BOUNDARY)
        y = random.randint(-BOUNDARY, BOUNDARY)
        self.goto(x, y)