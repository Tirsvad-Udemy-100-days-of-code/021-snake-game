# Snake Game (Day 21)

The classic Snake game, built object-oriented with Python's `turtle` module. It is
the day-21 assignment of Udemy's *100 Days of Code: The Complete Python Pro
Bootcamp*: a snake moves across a black 600 by 600 screen by itself and is steered
with the arrow keys; it eats food, grows, and a score is shown at the top; the game
is over when the head passes the wall or touches its own tail. Day 21 teaches class
inheritance (`Food` and `Scoreboard` inherit from `Turtle`) and slicing (the tail is
`segments[1:]`).

The game has no runtime dependencies. The code keeps the names of the lectures
(`Snake`, `create_snake`, `move`, `up`, `down`, `left`, `right`, `segments`,
`head`, `game_is_on`, `Food`, `Scoreboard`, `refresh`, `extend`, `increase_score`,
`game_over`) so that you can compare it with your own solution.

This repository continues
[020-snake-game](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/020-snake-game)
and starts from its finished game; `docs/project-plan.md` tells how the work is split.

> **Status:** the game is in the repository: `python -m snake_game` plays the whole
> game, adopted from the finished game of 020 together with its tests. The next
> milestone, `MIL-003`, checks it against the day-21 lectures and finishes this
> README.

## Requirements

- Python 3.13 or newer, with `tkinter` (the `turtle` module needs it).
- `git`, to clone the repository.
- Optional: [Doxygen](https://www.doxygen.nl/) to build the source documentation.
- No runtime dependencies. The development tools (`pytest`, `ruff`, `mypy`) are
  installed into the virtual environment by the `dev` extra.

## Set up

Clone the repository, then create a local virtual environment `.venv` in its
root, upgrade `pip` and install the project with its development tools. The
`.venv` folder is ignored by git.

```bash
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/021-snake-game.git
cd 021-snake-game
```

### Windows powershell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

If PowerShell refuses to run the activation script, allow scripts for this
window only with `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned`
and activate again. Python from python.org includes `tkinter`.

### Linux debian

Debian 13 or newer ships Python 3.13. On older releases install Python 3.13
separately.

```bash
sudo apt install python3 python3-venv python3-tk
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

### MacOS

```bash
brew install python@3.13 python-tk@3.13
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Run

With the virtual environment active:

```bash
python -m snake_game
```

It opens a black 600 by 600 window titled "My Snake Game". The snake of three
white squares starts in the middle and moves to the right by itself, 20 pixels
every 0.1 seconds.

| Key | Effect |
| --- | --- |
| Up, Down, Left, Right | Turn the snake |

The snake never turns straight back onto itself: the arrow key opposite to the
way it is going is ignored, even when two keys are pressed within one move.

A small blue circle, the food, appears at a random place. When the head comes closer
to it than 15 pixels the snake eats it: the food moves to a new random place, the
snake grows by one segment, and the score at the top of the window goes up by 1
(`Score: 0`, `Score: 1`, ...).

The game is over when the head passes the wall (more than 280 pixels from the centre
on any side) or touches the tail (comes closer than 10 pixels to a segment behind it).
The snake stops, the text `GAME OVER` appears in the middle of the window, the score
stays where it is, and a click on the window closes it. You can also close the window
with its close button at any time.

## Run the tests

The tests need no display: they use fakes instead of real turtles.

```bash
pytest
```

The same checks that continuous integration runs:

```bash
python -m pytest
python -m ruff check src tests
python -m ruff format --check src tests
python -m mypy
```

## Continuous integration

`.gitea/workflows/ci.yml` runs on Gitea Actions on every push and on every pull
request. It sets up Python 3.13, upgrades `pip`, installs `.[dev]`, then runs
`pytest`, `ruff` (lint and format check) and `mypy`. It does not build the source
documentation: run `doxygen Doxyfile` yourself, as the next section shows. No
step opens a turtle window.

The workflow lives in `.gitea/workflows` and not in `.github/workflows`, so
GitHub does not run it and pushing to the GitHub mirror needs no workflow
permission.

## Build the source documentation

The source is documented with Doxygen comments and the `Doxyfile` in the root.
Install Doxygen (`winget install DimitriVanHeesch.Doxygen` on Windows,
`sudo apt install doxygen` on Debian, `brew install doxygen` on macOS), then:

```bash
doxygen Doxyfile
```

The HTML is written to `build/doxygen/index.html`. A warning fails the build.

## Project layout

```text
.
├── .gitea/workflows/ci.yml    continuous integration (Gitea Actions)
├── docs/                      business case, plan, milestones, reviews
├── src/snake_game/            the game
│   ├── __init__.py
│   ├── __main__.py            starts the game: python -m snake_game
│   ├── constants.py           every constant of the game
│   ├── food.py                the Food class (inherits from Turtle)
│   ├── main.py                screen set-up and the main flow
│   ├── scoreboard.py          the Scoreboard class (inherits from Turtle)
│   └── snake.py               the Snake class
├── tests/                     pytest tests (fakes.py holds the fake turtle and screen)
├── Doxyfile                   source documentation settings
├── LICENSE
├── pyproject.toml             project configuration
└── README.md
```

## License

GNU Affero General Public License v3.0 only. See [LICENSE](LICENSE).
