
from turtle import Turtle


class Border:
    def __init__(self, size=410):
        """
        Draws a square border.
        size = half of window size (800x800 → 400)
        """
        self.border = Turtle()
        self.border.hideturtle()
        self.border.color("MidnightBlue")
        self.border.pensize(4)
        self.border.penup()

        start = size - 20  # keeps border slightly inside window
        self.border.goto(-start, start)
        self.border.pendown()

        for _ in range(4):
            self.border.forward(start * 2)
            self.border.right(90)