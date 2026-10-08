"""Tests of the scoreboard, with a fake `Turtle` as its base class."""

import importlib
import sys

import pytest

from fakes import install_fake_turtle, make_scoreboard
from snake_game import constants

START_TEXT = ("write", ("Score: 0", "center", ("Arial", 24, "normal")))


def test_scoreboard_is_white_hidden_and_at_the_top_centre(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    scoreboard = make_scoreboard(monkeypatch)

    assert ("color", ("white",)) in scoreboard.calls
    assert "penup" in scoreboard.call_names()
    assert "hideturtle" in scoreboard.call_names()
    assert ("goto", constants.SCOREBOARD_POSITION) in scoreboard.calls


def test_scoreboard_inherits_from_turtle(monkeypatch: pytest.MonkeyPatch) -> None:
    install_fake_turtle(monkeypatch)
    module = importlib.import_module("snake_game.scoreboard")

    assert issubclass(module.Scoreboard, sys.modules["turtle"].Turtle)


def test_scoreboard_starts_by_writing_score_0_centred_in_arial_24(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    scoreboard = make_scoreboard(monkeypatch)

    assert scoreboard.calls[-1] == START_TEXT


def test_increase_score_wipes_the_old_text_and_writes_the_new_score(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    scoreboard = make_scoreboard(monkeypatch)

    scoreboard.increase_score()

    assert scoreboard.call_names()[-2:] == ["clear", "write"]
    assert scoreboard.calls[-1] == (
        "write",
        ("Score: 1", "center", ("Arial", 24, "normal")),
    )


def test_every_food_adds_one_to_the_score(monkeypatch: pytest.MonkeyPatch) -> None:
    scoreboard = make_scoreboard(monkeypatch)

    for _ in range(3):
        scoreboard.increase_score()

    assert scoreboard.calls[-1][1][0] == "Score: 3"


def test_game_over_writes_the_text_at_the_centre_in_the_scoreboard_font(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    scoreboard = make_scoreboard(monkeypatch)

    scoreboard.game_over()

    assert scoreboard.calls[-2:] == [
        ("goto", constants.GAME_OVER_POSITION),
        ("write", ("GAME OVER", "center", ("Arial", 24, "normal"))),
    ]


def test_game_over_leaves_the_score_on_the_screen(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    scoreboard = make_scoreboard(monkeypatch)
    scoreboard.increase_score()
    calls_before = len(scoreboard.calls)

    scoreboard.game_over()

    assert "clear" not in scoreboard.call_names()[calls_before:]
