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

> **Status:** the project foundation is in place (environment, constants, tests,
> source documentation, continuous integration). The game itself, `python -m
> snake_game`, is added by the next milestone, `MIL-002`.

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

The game is not in the repository yet: `python -m snake_game` works once `MIL-002`
is merged, and this section is then completed with the keys, the food, the score
and the game-over rules.

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
│   └── constants.py           every constant of the game
├── tests/                     pytest tests
│   └── test_constants.py
├── Doxyfile                   source documentation settings
├── LICENSE
├── pyproject.toml             project configuration
└── README.md
```

The game modules (`snake.py`, `food.py`, `scoreboard.py`, `main.py`,
`__main__.py`) and their tests are added by `MIL-002`.

## License

GNU Affero General Public License v3.0 only. See [LICENSE](LICENSE).
