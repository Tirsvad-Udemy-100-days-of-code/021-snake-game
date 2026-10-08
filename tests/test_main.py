"""Tests of the main flow, with fakes instead of a real screen."""

import pytest

from fakes import (
    FakeFood,
    FakeScoreboard,
    FakeScreen,
    FakeTclError,
    FakeTerminatorError,
    imports_turtle_or_tkinter,
    install_fake_turtle,
    make_snake,
    script_randint,
)
from snake_game import constants
from snake_game.main import (
    bind_keys,
    configure_screen,
    eat_food_if_close,
    end_game_if_over,
    main,
    play_frame,
)

ARROW_KEYS = ("Up", "Down", "Left", "Right")


@pytest.fixture(autouse=True)
def food_far_away(monkeypatch: pytest.MonkeyPatch) -> None:
    """Make the food appear at the top right corner of the wall, far from the snake."""
    script_randint(monkeypatch, [])


@pytest.fixture
def sleeps(monkeypatch: pytest.MonkeyPatch) -> list[float]:
    """Replace `time.sleep` for one test and collect the waits requested."""
    waited: list[float] = []
    monkeypatch.setattr("time.sleep", waited.append)
    return waited


def test_configure_screen_sets_size_background_and_title_and_nothing_else() -> None:
    screen = FakeScreen()

    configure_screen(screen)

    assert screen.calls == [
        ("setup", (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)),
        ("bgcolor", (constants.SCREEN_BACKGROUND_COLOR,)),
        ("title", (constants.SCREEN_TITLE,)),
    ]


def test_bind_keys_listens_and_binds_the_four_arrow_keys_to_the_snake() -> None:
    screen = FakeScreen()
    snake, _ = make_snake()

    bind_keys(screen, snake)

    assert screen.call_names() == ["listen", "onkey", "onkey", "onkey", "onkey"]
    assert screen.bindings == {
        "Up": snake.up,
        "Down": snake.down,
        "Left": snake.left,
        "Right": snake.right,
    }


@pytest.mark.parametrize(
    ("key", "degrees"),
    [("Up", constants.UP), ("Down", constants.DOWN), ("Right", constants.RIGHT)],
)
def test_pressing_a_bound_key_turns_the_head(key: str, degrees: int) -> None:
    screen = FakeScreen()
    snake, _ = make_snake()
    bind_keys(screen, snake)

    screen.bindings[key]()

    assert snake.head.heading() == degrees


def test_play_frame_updates_the_screen_then_waits_then_moves(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    screen = FakeScreen(frames_before_close=1)
    snake, created = make_snake()
    seen: list[tuple[float, list[str], list[str]]] = []

    def record_sleep(seconds: float) -> None:
        seen.append((seconds, screen.call_names(), created[0].call_names()))

    monkeypatch.setattr("time.sleep", record_sleep)

    play_frame(screen, snake)

    assert len(seen) == 1
    seconds, screen_calls_at_sleep, head_calls_at_sleep = seen[0]
    assert seconds == constants.REFRESH_DELAY_SECONDS
    assert screen_calls_at_sleep == ["update"]
    assert "forward" not in head_calls_at_sleep
    assert "forward" in created[0].call_names()


def test_main_sets_up_the_screen_turns_off_drawing_and_binds_the_keys(
    monkeypatch: pytest.MonkeyPatch, sleeps: list[float]
) -> None:
    _, screens = install_fake_turtle(monkeypatch)

    main()

    assert len(screens) == 1
    assert screens[0].call_names()[:9] == [
        "setup",
        "bgcolor",
        "title",
        "tracer",
        "listen",
        "onkey",
        "onkey",
        "onkey",
        "onkey",
    ]
    assert ("tracer", (0,)) in screens[0].calls
    assert sorted(screens[0].bindings) == sorted(ARROW_KEYS)


def test_main_draws_the_snake_before_the_first_frame(
    monkeypatch: pytest.MonkeyPatch, sleeps: list[float]
) -> None:
    turtles, _ = install_fake_turtle(monkeypatch)

    main()

    snake_segments = turtles[: len(constants.STARTING_POSITIONS)]
    assert len(turtles) == len(constants.STARTING_POSITIONS) + 2  # food, scoreboard
    assert all(
        ("goto", position) in turtle.calls
        for turtle, position in zip(
            snake_segments, constants.STARTING_POSITIONS, strict=True
        )
    )


@pytest.mark.parametrize("closing_error", [FakeTerminatorError, FakeTclError])
def test_main_ends_quietly_when_the_window_is_closed(
    monkeypatch: pytest.MonkeyPatch,
    sleeps: list[float],
    closing_error: type[Exception],
) -> None:
    turtles, screens = install_fake_turtle(
        monkeypatch, frames_before_close=3, closing_error=closing_error
    )

    main()

    assert screens[0].call_names().count("update") == 3 + 1
    assert turtles[0].call_names().count("forward") == 3
    assert sleeps == [constants.REFRESH_DELAY_SECONDS] * 3
    assert "exitonclick" not in screens[0].call_names()


def test_main_lets_other_errors_through(
    monkeypatch: pytest.MonkeyPatch, sleeps: list[float]
) -> None:
    install_fake_turtle(monkeypatch, closing_error=KeyError)

    with pytest.raises(KeyError):
        main()


def test_the_snake_eats_food_closer_than_the_eating_distance() -> None:
    snake, created = make_snake()
    food = FakeFood(constants.FOOD_COLLISION_DISTANCE - 1, 0)
    scoreboard = FakeScoreboard()

    eat_food_if_close(snake, food, scoreboard)

    assert food.refreshes == 1
    assert scoreboard.increases == 1
    assert len(snake.segments) == len(created) == len(constants.STARTING_POSITIONS) + 1


@pytest.mark.parametrize(
    "place",
    [
        (constants.FOOD_COLLISION_DISTANCE, 0),
        (0, -constants.FOOD_COLLISION_DISTANCE),
        (2 * constants.FOOD_COLLISION_DISTANCE, 0),
        (200, 200),
    ],
)
def test_the_snake_does_not_eat_food_at_or_beyond_the_eating_distance(
    place: tuple[int, int],
) -> None:
    snake, _ = make_snake()
    food = FakeFood(*place)
    scoreboard = FakeScoreboard()

    eat_food_if_close(snake, food, scoreboard)

    assert food.refreshes == 0
    assert scoreboard.increases == 0
    assert len(snake.segments) == len(constants.STARTING_POSITIONS)


def test_the_snake_eats_food_that_is_close_diagonally() -> None:
    snake, _ = make_snake()
    food = FakeFood(10, 10)  # a distance of about 14.1
    scoreboard = FakeScoreboard()

    eat_food_if_close(snake, food, scoreboard)

    assert scoreboard.increases == 1


def test_main_lets_the_snake_eat_the_food_that_lies_on_its_way(
    monkeypatch: pytest.MonkeyPatch, sleeps: list[float]
) -> None:
    script_randint(monkeypatch, [20, 0])  # the first food lies one move ahead
    turtles, _ = install_fake_turtle(monkeypatch, frames_before_close=1)

    main()

    snake_head, _, _, food, scoreboard, new_segment = turtles
    assert snake_head.position() == (20, 0)
    assert [call for call in food.calls if call[0] == "goto"] == [
        ("goto", (20, 0)),
        ("goto", (constants.WALL_LIMIT, constants.WALL_LIMIT)),
    ]
    assert scoreboard.calls[-1][1][0] == "Score: 1"
    assert new_segment.position() == (-20, 0)  # where the last segment was


def test_main_does_not_raise_the_score_when_the_food_is_far_away(
    monkeypatch: pytest.MonkeyPatch, sleeps: list[float]
) -> None:
    turtles, _ = install_fake_turtle(monkeypatch, frames_before_close=3)

    main()

    scoreboard = turtles[4]
    assert scoreboard.calls[-1][1][0] == "Score: 0"
    assert len(turtles) == len(constants.STARTING_POSITIONS) + 2


def test_the_game_is_not_over_while_the_snake_is_inside_and_clear_of_its_tail() -> None:
    snake, _ = make_snake()
    scoreboard = FakeScoreboard()

    assert not end_game_if_over(snake, scoreboard)
    assert scoreboard.game_overs == 0


def test_the_game_is_over_when_the_head_passes_the_wall() -> None:
    snake, _ = make_snake()
    snake.head.goto(constants.WALL_LIMIT + 1, 0)
    scoreboard = FakeScoreboard()

    assert end_game_if_over(snake, scoreboard)
    assert scoreboard.game_overs == 1


def test_the_game_is_over_when_the_head_touches_the_tail() -> None:
    snake, created = make_snake()
    created[1].goto(3, 4)
    scoreboard = FakeScoreboard()

    assert end_game_if_over(snake, scoreboard)
    assert scoreboard.game_overs == 1


def test_main_ends_the_game_at_the_wall_shows_game_over_and_waits_for_a_click(
    monkeypatch: pytest.MonkeyPatch, sleeps: list[float]
) -> None:
    turtles, screens = install_fake_turtle(monkeypatch, frames_before_close=100)

    main()

    snake_head, scoreboard = turtles[0], turtles[4]
    moves_to_pass_the_wall = constants.WALL_LIMIT // constants.MOVE_DISTANCE + 1
    assert snake_head.call_names().count("forward") == moves_to_pass_the_wall
    assert snake_head.position() == (
        constants.MOVE_DISTANCE * moves_to_pass_the_wall,
        0,
    )
    assert scoreboard.calls[-1] == (
        "write",
        ("GAME OVER", "center", ("Arial", 24, "normal")),
    )
    assert screens[0].call_names()[-2:] == ["update", "exitonclick"]
    assert screens[0].call_names().count("exitonclick") == 1
    assert sleeps == [constants.REFRESH_DELAY_SECONDS] * moves_to_pass_the_wall


def test_main_ends_the_game_when_the_snake_touches_its_tail(
    monkeypatch: pytest.MonkeyPatch, sleeps: list[float]
) -> None:
    monkeypatch.setattr("snake_game.snake.Snake.hits_tail", lambda self: True)
    turtles, screens = install_fake_turtle(monkeypatch, frames_before_close=100)

    main()

    assert turtles[0].call_names().count("forward") == 1
    assert turtles[4].calls[-1][1][0] == "GAME OVER"
    assert screens[0].call_names()[-1] == "exitonclick"


def test_main_does_not_move_the_snake_after_game_over(
    monkeypatch: pytest.MonkeyPatch, sleeps: list[float]
) -> None:
    turtles, screens = install_fake_turtle(monkeypatch, frames_before_close=100)

    main()

    updates = screens[0].call_names().count("update")
    moves = turtles[0].call_names().count("forward")
    assert updates == moves + 1  # one update per frame, and one for the last text


@pytest.mark.parametrize("closing_error", [FakeTerminatorError, FakeTclError])
def test_main_ends_quietly_when_the_window_is_closed_after_game_over(
    monkeypatch: pytest.MonkeyPatch,
    sleeps: list[float],
    closing_error: type[Exception],
) -> None:
    moves_to_pass_the_wall = constants.WALL_LIMIT // constants.MOVE_DISTANCE + 1
    turtles, screens = install_fake_turtle(
        monkeypatch,
        frames_before_close=moves_to_pass_the_wall,
        closing_error=closing_error,
    )

    main()

    assert turtles[4].calls[-1][1][0] == "GAME OVER"
    assert "exitonclick" not in screens[0].call_names()


def test_importing_the_main_module_does_not_import_turtle_or_tkinter() -> None:
    assert not imports_turtle_or_tkinter("snake_game.main")
