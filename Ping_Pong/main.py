from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import pygame
import time


# -------------------------------------------------
# LOAD SOUNDS
# -------------------------------------------------
pygame.mixer.init()

theme_sound = pygame.mixer.Sound("sounds/theme.mp3")
ball_sound = pygame.mixer.Sound("sounds/ball.mp3")
score_sound = pygame.mixer.Sound("sounds/score.mp3")

# -------------------------------------------------
# SCREEN SETUP
# -------------------------------------------------
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PING PONG 🏓")
screen.tracer(0)

# Default background
screen.bgpic("assets/bg_dark.png")

# -------------------------------------------------
# GAME OBJECTS
# -------------------------------------------------
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

# -------------------------------------------------
# KEY STATE FLAGS (for smooth movement)
# -------------------------------------------------
keys = {
    "w": False,
    "s": False,
    "Up": False,
    "Down": False
}

# -------------------------------------------------
# PAUSE STATE
# -------------------------------------------------
paused = False

# -------------------------------------------------
# THEMES (background + contrasting colors)
# -------------------------------------------------
themes = [
    {
        "bg": "assets/bg_dark.png",
        "paddle": "white",
        "ball": "white",
        "score": "red"
    },
    {
        "bg": "assets/bg.gif",
        "paddle": "#262c37",
        "ball": "#c53a3a",
        "score": "#3f495b"
    },
    {
        "bg": "assets/bg1.png",
        "paddle": "#38bdf8",
        "ball": "#fb7185",
        "score": "#ffffff"
    }
]

current_theme = 0

# -------------------------------------------------
# INPUT HANDLERS
# -------------------------------------------------
def key_press(k):
    keys[k] = True

def key_release(k):
    keys[k] = False


def toggle_pause():
    """
    Toggles pause AND pauses/resumes theme music
    without restarting or looping the song.
    """
    global paused
    paused = not paused

    if paused:
        theme_channel.pause()
    else:
        theme_channel.unpause()


def change_theme():
    """
    Cycles background image and applies
    contrasting colors safely.
    """
    global current_theme
    current_theme = (current_theme + 1) % len(themes)
    theme = themes[current_theme]

    screen.bgpic(theme["bg"])
    l_paddle.color(theme["paddle"])
    r_paddle.color(theme["paddle"])
    ball.color(theme["ball"])
    scoreboard.color(theme["score"])
    scoreboard.update_score()

# -------------------------------------------------
# KEY BINDINGS
# -------------------------------------------------
screen.listen()

for key in keys:
    screen.onkeypress(lambda k=key: key_press(k), key)
    screen.onkeyrelease(lambda k=key: key_release(k), key)

screen.onkey(toggle_pause, "p")
screen.onkey(toggle_pause, "P")

screen.onkey(change_theme, "t")
screen.onkey(change_theme, "T")
# -------------------------------------------------
# START THEME MUSIC (PLAY ONCE ONLY)
# -------------------------------------------------
theme_sound.set_volume(0.3)
theme_channel = theme_sound.play(loops=0)

# -------------------------------------------------
# GAME LOOP
# -------------------------------------------------
game_on = True
while game_on:
    screen.update()

    # ⏸ Pause freezes gameplay only
    if paused:
        continue

    time.sleep(ball.move_speed)
    ball.move()

    # Paddle continuous movement
    if keys["w"]:
        l_paddle.move_up()
    if keys["s"]:
        l_paddle.move_down()
    if keys["Up"]:
        r_paddle.move_up()
    if keys["Down"]:
        r_paddle.move_down()

    # Wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Paddle collision
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or \
       (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        ball_sound.play()

    # Score update
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        score_sound.play()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        score_sound.play()

screen.exitonclick()