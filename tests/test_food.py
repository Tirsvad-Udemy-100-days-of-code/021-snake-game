"""Tests of the food, with a fake `Turtle` as its base class."""

import importlib
import sys

import pytest

from fakes import install_fake_turtle, make_food, script_randint
from snake_game import constants


def test_food_is_a_blue_half_size_circle_with_the_pen_up_and_no_animation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    food = make_food(monkeypatch)

    assert ("shape", ("circle",)) in food.calls
    assert ("shapesize", (0.5, 0.5)) in food.calls
    assert ("color", ("blue",)) in food.calls
    assert ("speed", ("fastest",)) in food.calls
    assert "penup" in food.call_names()


def test_food_inherits_from_turtle_and_calls_the_base_class_first(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    install_fake_turtle(monkeypatch)
    module = importlib.import_module("snake_game.food")

    food = module.Food()

    assert issubclass(module.Food, sys.modules["turtle"].Turtle)
    assert food.calls[0][0] == "shape"  # the base class set up `calls` before


def test_food_starts_at_a_random_place(monkeypatch: pytest.MonkeyPatch) -> None:
    script_randint(monkeypatch, [12, -34])

    food = make_food(monkeypatch)

    assert food.position() == (12, -34)


def test_refresh_moves_the_food_to_a_new_random_place(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    script_randint(monkeypatch, [1, 2, 3, 4])
    food = make_food(monkeypatch)

    food.refresh()

    assert food.position() == (3, 4)


def test_random_coordinate_asks_for_a_number_from_wall_to_wall(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    bounds = script_randint(monkeypatch, [7])
    install_fake_turtle(monkeypatch)
    module = importlib.import_module("snake_game.food")

    result = module.random_coordinate()

    assert result == 7
    assert bounds == [(-constants.WALL_LIMIT, constants.WALL_LIMIT)]


def test_random_places_are_always_inside_the_walls(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    install_fake_turtle(monkeypatch)
    module = importlib.import_module("snake_game.food")

    places = [module.random_coordinate() for _ in range(500)]

    wall = constants.WALL_LIMIT
    assert all(-wall <= place <= wall for place in places)
