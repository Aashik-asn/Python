
from turtle import Turtle

ALIGN = "center"
FONT = ("Born2bSportyFS", 24, "normal")
GAME_OVER_FONT = ("Born2bSportyFS", 36, "normal")


class Scoreboard:
    def __init__(self):
        # Turtle for score / high score
        self.score_turtle = Turtle()
        self.score_turtle.penup()
        self.score_turtle.hideturtle()
        self.score_turtle.goto(220, 350)

        # Turtle for GAME OVER
        self.game_over_turtle = Turtle()
        self.game_over_turtle.penup()
        self.game_over_turtle.hideturtle()

        self.score = 0
        self.text_color = "black"  # default

        with open("high_score.txt") as file:
            self.high_score = int(file.read())

        self.update_score()

    def set_color(self, color):
        """
        Change score & high score text color
        (used by theme selector)
        """
        self.text_color = color
        self.update_score()

    def update_score(self):
        self.score_turtle.clear()
        self.score_turtle.color(self.text_color)
        self.score_turtle.write(
            f"SCORE : {self.score}  HIGH SCORE : {self.high_score}",
            align=ALIGN,
            font=FONT
        )

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.clear_game_over()
        self.update_score()

    def game_over(self):
        self.game_over_turtle.goto(0, 0)
        self.game_over_turtle.write(
            "GAME OVER",
            align="center",
            font=GAME_OVER_FONT
        )

    def clear_game_over(self):
        self.game_over_turtle.clear()