"""! @file
@brief The main flow of the game: set up the screen, draw the snake and run it.

The flow follows the lectures "Screen Setup and Creating a Snake Body",
"Animating the Snake Segments on Screen" and "Controlling the Snake with
Keypresses", and the day-21 steps in which the snake eats food, the score rises and
the game ends.
"""

import time
from collections.abc import Callable
from typing import Protocol

from snake_game.constants import (
    FOOD_COLLISION_DISTANCE,
    REFRESH_DELAY_SECONDS,
    SCREEN_BACKGROUND_COLOR,
    SCREEN_HEIGHT,
    SCREEN_TITLE,
    SCREEN_WIDTH,
)
from snake_game.snake import Snake


class ScreenLike(Protocol):
    """! @brief What the helper functions need from the screen.

    A `turtle.Screen` fits this description, and so does a fake in a test.
    """

    def setup(self, width: float, height: float) -> None:
        """! @brief Set the size of the window.

        @param width Width in pixels.
        @param height Height in pixels.
        """
        ...

    def bgcolor(self, color: str, /) -> None:
        """! @brief Set the background colour.

        @param color Name of the colour, for example `black`.
        """
        ...

    def title(self, titlestring: str, /) -> None:
        """! @brief Set the title of the window.

        @param titlestring The title.
        """
        ...

    def update(self) -> None:
        """! @brief Draw everything that has changed since the last update."""
        ...

    def listen(self) -> None:
        """! @brief Make the screen receive the key presses."""
        ...

    def onkey(self, fun: Callable[[], object], key: str) -> None:
        """! @brief Call a function when a key is pressed.

        @param fun The function to call.
        @param key Name of the key, for example `Up`.
        """
        ...


class FoodLike(Protocol):
    """! @brief What `eat_food_if_close` needs from the food.

    A `Food` fits this description, and so does a fake in a test.
    """

    def refresh(self) -> None:
        """! @brief Move the food to a new random place."""
        ...

    def position(self) -> tuple[float, float]:
        """! @brief Tell where the food is.

        @return The x and y coordinates.
        """
        ...


class ScoreboardLike(Protocol):
    """! @brief What the eating and game-over checks need from the scoreboard.

    A `Scoreboard` fits this description, and so does a fake in a test.
    """

    def increase_score(self) -> None:
        """! @brief Add 1 to the score and write it."""
        ...

    def game_over(self) -> None:
        """! @brief Write the game-over text."""
        ...


def configure_screen(screen: ScreenLike) -> None:
    """! @brief Give the screen the size, background colour and title of the game.

    @param screen The screen to set up.
    """
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor(SCREEN_BACKGROUND_COLOR)
    screen.title(SCREEN_TITLE)


def bind_keys(screen: ScreenLike, snake: Snake) -> None:
    """! @brief Turn the snake with the arrow keys.

    @param screen The screen that receives the key presses.
    @param snake The snake to steer.
    """
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


def play_frame(screen: ScreenLike, snake: Snake) -> None:
    """! @brief Show the snake, wait for `REFRESH_DELAY_SECONDS`, then move it.

    This is one pass of the animation loop. The screen is updated by hand because
    automatic drawing is off, so the whole snake appears at once.

    @param screen The screen to update.
    @param snake The snake to move.
    """
    screen.update()
    time.sleep(REFRESH_DELAY_SECONDS)
    snake.move()


def eat_food_if_close(snake: Snake, food: FoodLike, scoreboard: ScoreboardLike) -> None:
    """! @brief Let the snake eat the food when the head is close enough to it.

    Eating moves the food to a new place, makes the snake one segment longer and
    adds 1 to the score. The head must be closer than `FOOD_COLLISION_DISTANCE`.

    @param snake The snake.
    @param food The food.
    @param scoreboard The scoreboard that shows the score.
    """
    if snake.head.distance(food.position()) < FOOD_COLLISION_DISTANCE:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


def end_game_if_over(snake: Snake, scoreboard: ScoreboardLike) -> bool:
    """! @brief End the game when the head passes the wall or touches the tail.

    When the game is over the scoreboard writes the game-over text.

    @param snake The snake.
    @param scoreboard The scoreboard that writes the game-over text.
    @return True when the game is over.
    """
    if snake.hits_wall() or snake.hits_tail():
        scoreboard.game_over()
        return True
    return False


def main() -> None:
    """! @brief Open the game window and run the snake until the window is closed.

    Closing the window during the animation loop makes `screen.update()` raise
    `tkinter.TclError` ("invalid command name"), and `turtle` raises
    `turtle.Terminator` in some other calls once its window is gone. Both mean
    "the player closed the window", so the game ends quietly with exit code 0.
    When the snake passes the wall or touches its tail the loop ends, the screen is
    updated so that the game-over text shows, and `screen.exitonclick()` waits for a
    click.

    `turtle` and `tkinter` are imported here and not at the top of the module, and
    so are `food` and `scoreboard`, whose classes inherit from `Turtle`: importing
    this module needs neither a display nor `tkinter`.
    """
    from tkinter import TclError
    from turtle import Screen, Terminator

    from snake_game.food import Food
    from snake_game.scoreboard import Scoreboard

    screen = Screen()
    configure_screen(screen)
    screen.tracer(0)
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    bind_keys(screen, snake)

    game_is_on = True
    try:
        while game_is_on:
            play_frame(screen, snake)
            eat_food_if_close(snake, food, scoreboard)
            if end_game_if_over(snake, scoreboard):
                game_is_on = False
        screen.update()
        screen.exitonclick()
    except (Terminator, TclError):
        return  # the window was closed: there is nothing left to do
