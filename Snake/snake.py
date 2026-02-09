
from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0


class Snake:
    def __init__(self):
        self.can_change_direction = True
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Create initial snake"""
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        """Add a new segment to the snake"""
        segment = Turtle("square")
        segment.color("black")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        """Add new segment at tail"""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move snake forward"""
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)

        self.head.forward(MOVE_DISTANCE)
        self.can_change_direction = True

    def up(self):
        if self.can_change_direction and self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.can_change_direction = False

    def down(self):
        if self.can_change_direction and self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.can_change_direction = False

    def left(self):
        if self.can_change_direction and self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.can_change_direction = False

    def right(self):
        if self.can_change_direction and self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.can_change_direction = False

    def reset(self):
        """Completely reset snake"""
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]