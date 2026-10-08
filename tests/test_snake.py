"""Tests of the snake, with fakes instead of real turtles."""

import math
from collections.abc import Sequence

import pytest

from fakes import (
    FakeSegment,
    imports_turtle_or_tkinter,
    install_fake_turtle,
    make_snake,
)
from snake_game import constants
from snake_game.snake import Segment, Snake

DIRECTIONS = {
    "up": constants.UP,
    "down": constants.DOWN,
    "left": constants.LEFT,
    "right": constants.RIGHT,
}
OPPOSITE = {
    constants.UP: constants.DOWN,
    constants.DOWN: constants.UP,
    constants.LEFT: constants.RIGHT,
    constants.RIGHT: constants.LEFT,
}


def positions(segments: Sequence[Segment]) -> list[tuple[float, float]]:
    """Return where every segment is, head first."""
    return [segment.position() for segment in segments]


def make_snake_moving(direction: int) -> tuple[Snake, list[FakeSegment]]:
    """Make a snake whose last move went in the given direction."""
    snake, created = make_snake()
    created[0].setheading(direction)
    snake.move()
    return snake, created


def test_snake_has_one_segment_per_starting_position() -> None:
    snake, _ = make_snake()

    assert len(snake.segments) == len(constants.STARTING_POSITIONS) == 3


def test_segments_are_the_created_turtles_in_order() -> None:
    snake, created = make_snake()

    assert snake.segments == created


def test_segments_are_white_squares() -> None:
    _, created = make_snake()

    for segment in created:
        assert ("shape", ("square",)) in segment.calls
        assert ("color", ("white",)) in segment.calls


def test_segments_are_placed_at_the_starting_positions_head_first() -> None:
    _, created = make_snake()

    assert positions(created) == [
        (float(x), float(y)) for x, y in constants.STARTING_POSITIONS
    ]


def test_pen_is_lifted_before_a_segment_is_moved() -> None:
    _, created = make_snake()

    for segment in created:
        names = segment.call_names()
        assert names.count("goto") == 1
        assert names.index("penup") < names.index("goto")


def test_create_snake_adds_three_more_segments_when_called_again() -> None:
    snake, _ = make_snake()

    snake.create_snake()

    assert len(snake.segments) == 2 * len(constants.STARTING_POSITIONS)


def test_default_segment_factory_makes_turtles(monkeypatch: pytest.MonkeyPatch) -> None:
    turtles, _ = install_fake_turtle(monkeypatch)

    snake = Snake()

    assert snake.segments == turtles
    assert len(turtles) == len(constants.STARTING_POSITIONS)


def test_importing_the_snake_module_does_not_import_turtle_or_tkinter() -> None:
    assert not imports_turtle_or_tkinter("snake_game.snake")


def test_head_is_the_first_segment() -> None:
    snake, created = make_snake()

    assert snake.head is created[0]


def test_snake_starts_moving_to_the_right() -> None:
    snake, _ = make_snake()

    assert snake.head.heading() == constants.RIGHT


def test_move_goes_forward_by_the_move_distance() -> None:
    snake, created = make_snake()

    snake.move()

    assert ("forward", (constants.MOVE_DISTANCE,)) in created[0].calls
    assert created[0].position() == (constants.MOVE_DISTANCE, 0)


def test_move_takes_each_segment_to_the_place_of_the_one_before_it() -> None:
    snake, created = make_snake()

    snake.move()

    assert positions(created) == [(20, 0), (0, 0), (-20, 0)]


def test_move_keeps_the_segments_joined_while_turning() -> None:
    snake, created = make_snake()

    snake.up()
    snake.move()
    snake.move()

    assert positions(created) == [(0, 40), (0, 20), (0, 0)]


def test_move_works_for_any_number_of_segments() -> None:
    snake, created = make_snake()
    for index in range(3, 6):
        extra = FakeSegment()
        extra.goto(-20 * index, 0)
        snake.segments.append(extra)
        created.append(extra)

    snake.move()

    assert positions(created) == [
        (20, 0),
        (0, 0),
        (-20, 0),
        (-40, 0),
        (-60, 0),
        (-80, 0),
    ]


@pytest.mark.parametrize("travel", list(OPPOSITE))
@pytest.mark.parametrize("method", list(DIRECTIONS))
def test_every_turn_is_accepted_unless_it_is_a_reversal(
    method: str, travel: int
) -> None:
    snake, _ = make_snake_moving(travel)

    getattr(snake, method)()

    wanted = DIRECTIONS[method]
    is_reversal = wanted == OPPOSITE[travel]
    assert snake.head.heading() == (travel if is_reversal else wanted)


def test_up_sets_the_head_to_90_degrees() -> None:
    snake, _ = make_snake()

    snake.up()

    assert snake.head.heading() == 90


def test_down_sets_the_head_to_270_degrees() -> None:
    snake, _ = make_snake()

    snake.down()

    assert snake.head.heading() == 270


def test_right_keeps_the_head_at_0_degrees() -> None:
    snake, _ = make_snake()

    snake.right()

    assert snake.head.heading() == 0


def test_left_is_ignored_while_moving_right() -> None:
    snake, _ = make_snake()

    snake.left()

    assert snake.head.heading() == 0


def test_two_key_presses_within_one_move_do_not_reverse_the_snake() -> None:
    snake, _ = make_snake()

    snake.up()
    snake.left()

    assert snake.head.heading() == constants.UP


def test_a_turn_is_accepted_after_the_move_that_followed_the_first_turn() -> None:
    snake, _ = make_snake()

    snake.up()
    snake.move()
    snake.left()

    assert snake.head.heading() == constants.LEFT


def test_add_segment_puts_a_white_square_with_the_pen_up_at_the_position() -> None:
    snake, created = make_snake()

    snake.add_segment((100, -60))

    new = created[-1]
    assert snake.segments[-1] is new
    assert ("shape", ("square",)) in new.calls
    assert ("color", ("white",)) in new.calls
    assert new.call_names().index("penup") < new.call_names().index("goto")
    assert new.position() == (100, -60)


def test_extend_adds_one_segment_where_the_last_segment_is() -> None:
    snake, created = make_snake()
    last_place = created[-1].position()

    snake.extend()

    assert len(snake.segments) == len(constants.STARTING_POSITIONS) + 1
    assert snake.segments[-1].position() == last_place


def test_extend_twice_adds_two_segments() -> None:
    snake, _ = make_snake()

    snake.extend()
    snake.extend()

    assert len(snake.segments) == len(constants.STARTING_POSITIONS) + 2


def test_head_stays_the_first_segment_after_extend() -> None:
    snake, created = make_snake()

    snake.extend()

    assert snake.head is created[0]
    assert snake.segments[0] is created[0]


def test_the_new_segment_follows_the_snake_and_the_body_stays_joined_when_turning() -> (
    None
):
    snake, _ = make_snake()
    snake.up()
    snake.move()
    snake.extend()

    snake.move()

    places = positions(snake.segments)
    gaps = [
        math.dist(places[index], places[index + 1]) for index in range(len(places) - 1)
    ]
    assert gaps == [constants.MOVE_DISTANCE] * (len(places) - 1)


@pytest.mark.parametrize(
    "place", [(281, 0), (-281, 0), (0, 281), (0, -281), (300, 300), (0, 1000)]
)
def test_the_head_has_passed_the_wall_beyond_the_limit_on_any_side(
    place: tuple[int, int],
) -> None:
    snake, _ = make_snake()
    snake.head.goto(*place)

    assert snake.hits_wall()


@pytest.mark.parametrize(
    "place", [(0, 0), (280, 0), (-280, 0), (0, 280), (0, -280), (280, -280)]
)
def test_the_head_has_not_passed_the_wall_at_or_inside_the_limit(
    place: tuple[int, int],
) -> None:
    snake, _ = make_snake()
    snake.head.goto(*place)

    assert not snake.hits_wall()


@pytest.mark.parametrize("gap", [0, 5, 9])
def test_the_head_touches_the_tail_closer_than_the_touch_distance(gap: int) -> None:
    snake, created = make_snake()
    created[1].goto(gap, 0)

    assert snake.hits_tail()


@pytest.mark.parametrize("gap", [10, 11, 20, 100])
def test_the_head_does_not_touch_the_tail_at_or_beyond_the_touch_distance(
    gap: int,
) -> None:
    snake, created = make_snake()
    created[1].goto(gap, 0)

    assert not snake.hits_tail()


def test_the_head_touches_any_segment_of_a_long_tail() -> None:
    snake, created = make_snake()
    for index in range(3, 8):
        extra = FakeSegment()
        extra.goto(-20 * index, 0)
        snake.segments.append(extra)
        created.append(extra)
    created[6].goto(3, 4)  # a distance of 5 from the head, far down the tail

    assert snake.hits_tail()


def test_a_new_snake_does_not_touch_its_tail() -> None:
    snake, _ = make_snake()

    assert not snake.hits_tail()


def test_a_snake_with_only_a_head_has_no_tail_to_touch() -> None:
    snake, created = make_snake()
    snake.segments[:] = [created[0]]
    created[0].goto(0, 0)

    assert not snake.hits_tail()


def test_the_new_segment_after_growing_does_not_touch_the_head() -> None:
    snake, _ = make_snake()
    snake.extend()
    snake.move()

    assert not snake.hits_tail()


def test_the_snake_hits_its_tail_when_it_turns_into_it() -> None:
    snake, created = make_snake()
    for index in range(3, 5):  # a snake of five segments
        extra = FakeSegment()
        extra.goto(-20 * index, 0)
        snake.segments.append(extra)
        created.append(extra)
    # Up, left and down, one move each, walk the head round a square of 20 by 20
    # pixels and back onto the place where the fifth segment is.
    for turn in (snake.up, snake.left, snake.down):
        turn()
        snake.move()

    assert snake.hits_tail()


def test_a_snake_of_four_segments_cannot_touch_its_tail_in_a_small_square() -> None:
    snake, created = make_snake()
    extra = FakeSegment()
    extra.goto(-60, 0)
    snake.segments.append(extra)
    created.append(extra)
    for turn in (snake.up, snake.left, snake.down):
        turn()
        snake.move()

    assert not snake.hits_tail()
