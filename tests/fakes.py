"""Fakes that stand in for turtles and the screen, so that no test opens a window."""

import importlib
import math
import os
import subprocess
import sys
import types
from collections.abc import Callable, Sequence
from pathlib import Path
from typing import Any

import pytest

from snake_game.snake import Snake

SRC = Path(__file__).resolve().parents[1] / "src"
# Modules whose classes inherit from `Turtle`: they bind their base class when they
# are imported, so each test that installs the fake `turtle` module imports them anew.
INHERITING_MODULES = ("snake_game.food", "snake_game.scoreboard")


class FakeTerminatorError(Exception):
    """Stands in for `turtle.Terminator`."""


class FakeTclError(Exception):
    """Stands in for `tkinter.TclError`."""


class FakeSegment:
    """A turtle that records what is done to it, in order, and keeps its state.

    It is a segment of the snake, and also the base class that stands in for
    `turtle.Turtle` when `Food` and `Scoreboard` are tested.
    """

    def __init__(self) -> None:
        self.calls: list[tuple[str, tuple[object, ...]]] = []
        self.x = 0.0
        self.y = 0.0
        self.angle = 0.0

    def shape(self, name: str, /) -> None:
        self.calls.append(("shape", (name,)))

    def shapesize(self, stretch_wid: float, stretch_len: float) -> None:
        self.calls.append(("shapesize", (stretch_wid, stretch_len)))

    def color(self, color: str, /) -> None:
        self.calls.append(("color", (color,)))

    def speed(self, speed: str) -> None:
        self.calls.append(("speed", (speed,)))

    def penup(self) -> None:
        self.calls.append(("penup", ()))

    def hideturtle(self) -> None:
        self.calls.append(("hideturtle", ()))

    def clear(self) -> None:
        self.calls.append(("clear", ()))

    def write(
        self,
        arg: str,
        align: str = "left",
        font: tuple[str, int, str] = ("Arial", 8, "normal"),
    ) -> None:
        self.calls.append(("write", (arg, align, font)))

    def goto(self, x: float | tuple[float, float], y: float | None = None, /) -> None:
        if isinstance(x, tuple):
            x, y = x
        assert y is not None
        self.calls.append(("goto", (x, y)))
        self.x, self.y = x, y

    def xcor(self) -> float:
        return self.x

    def ycor(self) -> float:
        return self.y

    def position(self) -> tuple[float, float]:
        return (self.x, self.y)

    def distance(self, x: tuple[float, float], /) -> float:
        return math.hypot(self.x - x[0], self.y - x[1])

    def forward(self, distance: float, /) -> None:
        self.calls.append(("forward", (distance,)))
        radians = math.radians(self.angle)
        self.x += round(distance * math.cos(radians), 10)
        self.y += round(distance * math.sin(radians), 10)

    def heading(self) -> float:
        return self.angle

    def setheading(self, to_angle: float, /) -> None:
        self.calls.append(("setheading", (to_angle,)))
        self.angle = float(to_angle) % 360

    def call_names(self) -> list[str]:
        """Return the names of the calls, in the order they were made."""
        return [name for name, _ in self.calls]


class FakeFood:
    """A food that counts how often it was moved."""

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
        self.refreshes = 0

    def refresh(self) -> None:
        self.refreshes += 1

    def position(self) -> tuple[float, float]:
        return (self.x, self.y)


class FakeScoreboard:
    """A scoreboard that counts how often the score was raised."""

    def __init__(self) -> None:
        self.increases = 0
        self.game_overs = 0

    def increase_score(self) -> None:
        self.increases += 1

    def game_over(self) -> None:
        self.game_overs += 1


class FakeScreen:
    """A screen that records what is done to it, in order.

    After `frames_before_close` updates it behaves like a closed window: the next
    `update` raises `closing_error`.
    """

    def __init__(
        self,
        frames_before_close: int = 0,
        closing_error: type[Exception] = FakeTerminatorError,
    ) -> None:
        self.calls: list[tuple[str, tuple[object, ...]]] = []
        self.bindings: dict[str, Callable[[], object]] = {}
        self._updates_left = frames_before_close
        self._closing_error = closing_error

    def setup(self, width: float, height: float) -> None:
        self.calls.append(("setup", (width, height)))

    def bgcolor(self, color: str, /) -> None:
        self.calls.append(("bgcolor", (color,)))

    def title(self, titlestring: str, /) -> None:
        self.calls.append(("title", (titlestring,)))

    def tracer(self, n: int, /) -> None:
        self.calls.append(("tracer", (n,)))

    def listen(self) -> None:
        self.calls.append(("listen", ()))

    def onkey(self, fun: Callable[[], object], key: str) -> None:
        self.calls.append(("onkey", (key,)))
        self.bindings[key] = fun

    def update(self) -> None:
        self.calls.append(("update", ()))
        if self._updates_left == 0:
            raise self._closing_error
        self._updates_left -= 1

    def exitonclick(self) -> None:
        self.calls.append(("exitonclick", ()))

    def call_names(self) -> list[str]:
        """Return the names of the calls, in the order they were made."""
        return [name for name, _ in self.calls]


def make_snake() -> tuple[Snake, list[FakeSegment]]:
    """Make a snake whose segments are fakes, and return the fakes too."""
    created: list[FakeSegment] = []

    def factory() -> FakeSegment:
        segment = FakeSegment()
        created.append(segment)
        return segment

    return Snake(segment_factory=factory), created


def install_fake_turtle(
    monkeypatch: pytest.MonkeyPatch,
    *,
    frames_before_close: int = 0,
    closing_error: type[Exception] = FakeTerminatorError,
) -> tuple[list[FakeSegment], list[FakeScreen]]:
    """Replace the `turtle` and `tkinter` modules with fakes for one test.

    The fake screen acts like a window that the player closes after
    `frames_before_close` updates, by raising `closing_error` from `update`.
    Every turtle the code under test creates, including a `Food` or a `Scoreboard`
    whose base class is the fake `Turtle`, is added to the first list returned;
    every screen is added to the second. `food` and `scoreboard` are forgotten, so
    that they are imported again against the fake and removed again after the test.
    """
    segments: list[FakeSegment] = []
    screens: list[FakeScreen] = []

    class RegisteredSegment(FakeSegment):
        def __init__(self) -> None:
            super().__init__()
            segments.append(self)

    def make_screen() -> FakeScreen:
        screen = FakeScreen(frames_before_close, closing_error)
        screens.append(screen)
        return screen

    turtle_module = types.ModuleType("turtle")
    turtle_module.__dict__["Turtle"] = RegisteredSegment
    turtle_module.__dict__["Screen"] = make_screen
    turtle_module.__dict__["Terminator"] = FakeTerminatorError
    tkinter_module = types.ModuleType("tkinter")
    tkinter_module.__dict__["TclError"] = FakeTclError
    monkeypatch.setitem(sys.modules, "turtle", turtle_module)
    monkeypatch.setitem(sys.modules, "tkinter", tkinter_module)
    for name in INHERITING_MODULES:
        # Set, then delete: when the test ends monkeypatch undoes both in reverse
        # order and the key is gone again, whatever the test imported meanwhile.
        monkeypatch.setitem(sys.modules, name, types.ModuleType(name))
        monkeypatch.delitem(sys.modules, name)
    return segments, screens


def script_randint(
    monkeypatch: pytest.MonkeyPatch, values: Sequence[int]
) -> list[tuple[int, int]]:
    """Make `random.randint` return the given values in turn, then the upper bound.

    Returns the list that collects the bounds of every call.
    """
    queue = iter(values)
    bounds: list[tuple[int, int]] = []

    def fake_randint(low: int, high: int) -> int:
        bounds.append((low, high))
        return next(queue, high)

    monkeypatch.setattr("random.randint", fake_randint)
    return bounds


def make_food(monkeypatch: pytest.MonkeyPatch) -> Any:
    """Make a real `Food` whose base class is the fake `Turtle`.

    The result is typed `Any` because it has the methods of `Food` (`refresh`) and
    the recording methods of the fake base class (`calls`, `position`) at once.
    """
    install_fake_turtle(monkeypatch)
    module = importlib.import_module("snake_game.food")
    return module.Food()


def make_scoreboard(monkeypatch: pytest.MonkeyPatch) -> Any:
    """Make a real `Scoreboard` whose base class is the fake `Turtle`.

    The result is typed `Any` because it has the methods of `Scoreboard`
    (`increase_score`) and the recording methods of the fake base class (`calls`)
    at once.
    """
    install_fake_turtle(monkeypatch)
    module = importlib.import_module("snake_game.scoreboard")
    return module.Scoreboard()


def imports_turtle_or_tkinter(module_name: str) -> bool:
    """Tell whether importing a module in a fresh interpreter loads a display module."""
    code = (
        f"import sys, {module_name}; "
        "print('turtle' in sys.modules or 'tkinter' in sys.modules)"
    )
    result = subprocess.run(
        [sys.executable, "-c", code],
        env={**os.environ, "PYTHONPATH": str(SRC)},
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    return result.stdout.strip() == "True"
