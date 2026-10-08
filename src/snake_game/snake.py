"""! @file
@brief The snake: a list of square segments that the game draws and moves.

The class follows the lectures "Create a Snake Class & Move to OOP", "Animating
the Snake Segments on Screen" and "Controlling the Snake with Keypresses", and
the day-21 steps in which the snake grows and the game ends. It keeps the lectures'
names: `Snake`, `segments`, `create_snake`, `add_segment`, `extend`, `move`, `head`,
`up`, `down`, `left` and `right`. The only differences are that the snake gets
the function that makes a segment as a parameter, so that a test can pass a fake
and needs no window, and how a reversal is refused (see Snake).
"""

from collections.abc import Callable
from typing import Protocol

from snake_game.constants import (
    DOWN,
    LEFT,
    MOVE_DISTANCE,
    RIGHT,
    SEGMENT_COLOR,
    SEGMENT_SHAPE,
    STARTING_POSITIONS,
    TAIL_COLLISION_DISTANCE,
    UP,
    WALL_LIMIT,
)


class Segment(Protocol):
    """! @brief What the snake needs from one of its segments.

    A `turtle.Turtle` fits this description, and so does a fake in a test.
    """

    def shape(self, name: str, /) -> object:
        """! @brief Set the shape of the segment.

        @param name Name of the shape, for example `square`.
        @return Whatever the implementation returns; the snake ignores it.
        """
        ...

    def color(self, color: str, /) -> object:
        """! @brief Set the colour of the segment.

        @param color Name of the colour, for example `white`.
        @return Whatever the implementation returns; the snake ignores it.
        """
        ...

    def penup(self) -> None:
        """! @brief Lift the pen, so that moving the segment draws no line."""
        ...

    def goto(self, x: float, y: float, /) -> None:
        """! @brief Send the segment to a position.

        @param x The x coordinate.
        @param y The y coordinate.
        """
        ...

    def xcor(self) -> float:
        """! @brief Tell the x coordinate of the segment.

        @return The x coordinate.
        """
        ...

    def ycor(self) -> float:
        """! @brief Tell the y coordinate of the segment.

        @return The y coordinate.
        """
        ...

    def forward(self, distance: float, /) -> None:
        """! @brief Move the segment forward, in the direction it points.

        @param distance How far to move, in pixels.
        """
        ...

    def position(self) -> tuple[float, float]:
        """! @brief Tell where the segment is.

        @return The x and y coordinates.
        """
        ...

    def distance(self, x: tuple[float, float], /) -> float:
        """! @brief Tell how far the segment is from a position.

        @param x The x and y coordinates of the other place.
        @return The distance in pixels.
        """
        ...

    def heading(self) -> float:
        """! @brief Tell the direction the segment points, in degrees.

        @return The heading, 0 for right and growing counter-clockwise.
        """
        ...

    def setheading(self, to_angle: float, /) -> None:
        """! @brief Turn the segment to point in a direction.

        @param to_angle The heading in degrees.
        """
        ...


def make_turtle_segment() -> Segment:
    """! @brief Make a real turtle, the default way to get a segment.

    `turtle` is imported here and not at the top of the module, so that
    importing the snake needs neither a display nor `tkinter`.

    @return A new `turtle.Turtle`.
    """
    from turtle import Turtle

    return Turtle()


class Snake:
    """! @brief The snake of the game, drawn as a row of square segments.

    The snake cannot reverse onto itself. Like the lecture, a turn is refused when
    it points opposite to the way the snake is going. Unlike the lecture, "the way
    the snake is going" is the direction of its last move and not the current
    direction of the head: otherwise two key presses within one move (Up then Left
    while moving right) would turn the head twice and reverse the snake.
    """

    def __init__(self, segment_factory: Callable[[], Segment] | None = None) -> None:
        """! @brief Create the snake with its three starting segments.

        @param segment_factory Makes one new segment; defaults to a real turtle.
        """
        ## @brief Makes one new segment.
        self._segment_factory = segment_factory or make_turtle_segment
        ## @brief The segments of the snake, the head first.
        self.segments: list[Segment] = []
        self.create_snake()
        ## @brief The first segment, which leads the snake.
        self.head: Segment = self.segments[0]
        ## @brief The direction of the last move; a turn against it is refused.
        self._direction_of_travel: float = self.head.heading()

    def create_snake(self) -> None:
        """! @brief Draw one white square segment at each starting position.

        The segments are kept in `segments`, the head first.
        """
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position: tuple[float, float]) -> None:
        """! @brief Add a white square segment at the end of the snake.

        The pen is lifted before the segment is sent to its position, so no line is
        drawn.

        @param position The x and y coordinates of the new segment.
        """
        new_segment = self._segment_factory()
        new_segment.shape(SEGMENT_SHAPE)
        new_segment.color(SEGMENT_COLOR)
        new_segment.penup()
        new_segment.goto(*position)
        self.segments.append(new_segment)

    def extend(self) -> None:
        """! @brief Make the snake one segment longer.

        The new segment appears where the last segment is, and follows it on the
        next move.
        """
        self.add_segment(self.segments[-1].position())

    def move(self) -> None:
        """! @brief Move the snake one step along its path.

        Each segment, from the last to the second, goes to the place of the
        segment before it; then the head goes forward by `MOVE_DISTANCE`. Moving
        the tail first keeps the body joined while turning, however many segments
        there are.
        """
        for index in range(len(self.segments) - 1, 0, -1):
            ahead = self.segments[index - 1]
            self.segments[index].goto(ahead.xcor(), ahead.ycor())
        self.head.forward(MOVE_DISTANCE)
        self._direction_of_travel = self.head.heading()

    def hits_wall(self) -> bool:
        """! @brief Tell whether the head has passed the wall on any side.

        The head is outside when its x or its y is beyond `WALL_LIMIT`.

        @return True when the head is outside the wall.
        """
        return abs(self.head.xcor()) > WALL_LIMIT or abs(self.head.ycor()) > WALL_LIMIT

    def hits_tail(self) -> bool:
        """! @brief Tell whether the head touches the tail.

        The tail is every segment behind the head (a slice, `segments[1:]`). The head
        touches it when it is closer than `TAIL_COLLISION_DISTANCE` to one of them.
        A snake that has only a head has no tail to touch.

        @return True when the head touches a segment of the tail.
        """
        return any(
            self.head.distance(segment.position()) < TAIL_COLLISION_DISTANCE
            for segment in self.segments[1:]
        )

    def up(self) -> None:
        """! @brief Turn the head up, unless the snake is moving down."""
        if self._direction_of_travel != DOWN:
            self.head.setheading(UP)

    def down(self) -> None:
        """! @brief Turn the head down, unless the snake is moving up."""
        if self._direction_of_travel != UP:
            self.head.setheading(DOWN)

    def left(self) -> None:
        """! @brief Turn the head left, unless the snake is moving right."""
        if self._direction_of_travel != RIGHT:
            self.head.setheading(LEFT)

    def right(self) -> None:
        """! @brief Turn the head right, unless the snake is moving left."""
        if self._direction_of_travel != LEFT:
            self.head.setheading(RIGHT)
