"""! @file
@brief The food: a small dot that the snake eats.

The class follows the day-21 lecture on inheritance: `Food` is a `Turtle` that
sets itself up and moves to a random place. Because it inherits from `Turtle`,
this module needs `turtle` (and so `tkinter`) when it is imported; the game
imports it only when it starts, and the tests install a fake `turtle` module
first.
"""

import random
from turtle import Turtle

from snake_game.constants import (
    FOOD_COLOR,
    FOOD_SHAPE,
    FOOD_SIZE,
    FOOD_SPEED,
    WALL_LIMIT,
)


def random_coordinate() -> int:
    """! @brief Pick a random x or y inside the walls.

    All the randomness of the food comes from this one function, so that a test can
    replace it.

    @return A whole number from `-WALL_LIMIT` to `WALL_LIMIT`.
    """
    return random.randint(-WALL_LIMIT, WALL_LIMIT)


class Food(Turtle):
    """! @brief The food, a blue circle at a random place inside the walls."""

    def __init__(self) -> None:
        """! @brief Set the food up and put it at a random place."""
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.penup()
        self.shapesize(stretch_wid=FOOD_SIZE, stretch_len=FOOD_SIZE)
        self.color(FOOD_COLOR)
        self.speed(FOOD_SPEED)
        self.refresh()

    def refresh(self) -> None:
        """! @brief Move the food to a new random place inside the walls."""
        self.goto(random_coordinate(), random_coordinate())
