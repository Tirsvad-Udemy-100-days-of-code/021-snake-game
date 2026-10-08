## @file constants.py
#  @brief Constants of the snake game.
#
#  Every value that the day-20 and day-21 lectures fix lives here, so that no other
#  module contains a magic number. The turtle coordinate system has its centre
#  at (0, 0); the 600 by 600 screen therefore reaches from -300 to 300 on both
#  axes. A direction is a turtle heading in degrees: 0 points right and the
#  angle grows counter-clockwise.

"""Constants of the snake game, as fixed by the day-20 and day-21 lectures."""

from typing import Final

## @brief Width of the screen in pixels.
SCREEN_WIDTH: Final[int] = 600

## @brief Height of the screen in pixels.
SCREEN_HEIGHT: Final[int] = 600

## @brief Background colour of the screen.
SCREEN_BACKGROUND_COLOR: Final[str] = "black"

## @brief Title of the game window.
SCREEN_TITLE: Final[str] = "My Snake Game"

## @brief Shape of every segment of the snake.
SEGMENT_SHAPE: Final[str] = "square"

## @brief Colour of every segment of the snake.
SEGMENT_COLOR: Final[str] = "white"

## @brief Where the segments are drawn when the game starts, from head to tail.
#
#  The positions lie on one row, 20 pixels apart, which is the width of a
#  default turtle square, so the segments touch without overlapping.
STARTING_POSITIONS: Final[tuple[tuple[int, int], ...]] = ((0, 0), (-20, 0), (-40, 0))

## @brief Distance in pixels that the head moves in one move.
MOVE_DISTANCE: Final[int] = 20

## @brief Direction up, as a turtle heading in degrees.
UP: Final[int] = 90

## @brief Direction down, as a turtle heading in degrees.
DOWN: Final[int] = 270

## @brief Direction left, as a turtle heading in degrees.
LEFT: Final[int] = 180

## @brief Direction right, as a turtle heading in degrees.
RIGHT: Final[int] = 0

## @brief Wait in seconds between two moves.
REFRESH_DELAY_SECONDS: Final[float] = 0.1

## @brief Shape of the food.
FOOD_SHAPE: Final[str] = "circle"

## @brief Stretch factor of the food in both directions; 0.5 is half a default turtle.
FOOD_SIZE: Final[float] = 0.5

## @brief Colour of the food.
FOOD_COLOR: Final[str] = "blue"

## @brief Speed of the food; `fastest` switches its animation off.
FOOD_SPEED: Final[str] = "fastest"

## @brief How far from the centre the wall is, on every side, in pixels.
#
#  The head must stay inside it, and the food is shown inside it.
WALL_LIMIT: Final[int] = 280

## @brief The snake eats the food when the head is closer to it than this, in pixels.
FOOD_COLLISION_DISTANCE: Final[int] = 15

## @brief Text in front of the score on the scoreboard.
SCORE_LABEL: Final[str] = "Score: "

## @brief Colour of the scoreboard text.
SCOREBOARD_COLOR: Final[str] = "white"

## @brief Where the scoreboard text is written: the top centre of the screen.
SCOREBOARD_POSITION: Final[tuple[int, int]] = (0, 270)

## @brief Alignment of the scoreboard text around its position.
SCOREBOARD_ALIGNMENT: Final[str] = "center"

## @brief Font of the scoreboard text: family, size and style.
SCOREBOARD_FONT: Final[tuple[str, int, str]] = ("Arial", 24, "normal")

## @brief The head touches the tail when it is closer to a segment than this, in pixels.
TAIL_COLLISION_DISTANCE: Final[int] = 10

## @brief Text shown when the game is over.
GAME_OVER_TEXT: Final[str] = "GAME OVER"

## @brief Where the game-over text is written: the centre of the screen.
GAME_OVER_POSITION: Final[tuple[int, int]] = (0, 0)
