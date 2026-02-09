from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
from border import Border
import pygame



# Music
pygame.mixer.init()
eat_sound = pygame.mixer.Sound("sounds/eat.mp3")
game_over_sound = pygame.mixer.Sound("sounds/game_over.mp3")
pygame.mixer.music.load("sounds/bg.mp3")
pygame.mixer.music.play(-1)  # loop forever

# Screen setup
screen = Screen()
screen.setup(800, 800)
screen.bgcolor("GreenYellow")
screen.title("SNAKE 🐍")
screen.tracer(0)

# Game objects
border = Border()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

#Theme

THEMES = {
    "classic": {
        "bg": "GreenYellow",
        "snake": "black",
        "food": "HotPink",
        "score":"black"
    },
    "dark": {
        "bg": "black",
        "snake": "lime",
        "food": "red",
        "score": "lime"
    },
    "pastel": {
        "bg": "#F5F5F5",
        "snake": "#4CAF50",
        "food": "#FF4081",
        "score": "#4CAF50"
    }
}

current_theme = "classic"

def apply_theme():
    theme = THEMES[current_theme]
    screen.bgcolor(theme["bg"])
    for segment in snake.segments:
        segment.color(theme["snake"])
    food.color(theme["food"])
    scoreboard.set_color(theme["score"])

def change_theme():
    global current_theme
    keys = list(THEMES.keys())
    current_theme = keys[(keys.index(current_theme) + 1) % len(keys)]
    apply_theme()

# Game state
game_is_on = True
is_paused = False
game_speed = 0.12


# -------- CONTROLS -------- #

def restart_game():
    global game_is_on, game_speed, is_paused
    game_is_on = True
    game_speed = 0.12
    snake.reset()
    food.refresh()
    scoreboard.reset_score()
    if not is_paused:
        pygame.mixer.music.play(-1)


def toggle_pause():
    global is_paused
    is_paused = not is_paused
    if not is_paused and game_is_on:
        pygame.mixer.music.load("sounds/bg.mp3")
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.stop()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
screen.onkey(restart_game, "r")
screen.onkey(toggle_pause, "p")
screen.onkey(change_theme, "t")

# -------- GAME LOOP -------- #

while True:
    screen.update()
    time.sleep(game_speed)

    if not is_paused and game_is_on:
        snake.move()

        # Food collision
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()
            game_speed = max(0.05, game_speed - 0.005)
            eat_sound.play()
        #border collision
        BORDER_LIMIT = 380  # must match border placement

        if (
                snake.head.xcor() > BORDER_LIMIT
                or snake.head.xcor() < -BORDER_LIMIT
                or snake.head.ycor() > BORDER_LIMIT
                or snake.head.ycor() < -BORDER_LIMIT
        ):
            game_is_on = False
            scoreboard.game_over()
            game_over_sound.play()
            pygame.mixer.music.stop()

        # Tail collision
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()
                game_over_sound.play()
                pygame.mixer.music.stop()

screen.exitonclick()