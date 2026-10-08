# Business Case: Snake Game (Day 21)

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-08 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version, reviewed in RC-001 (Go) | pending |

---

## Executive Summary

Snake Game (Day 21) is the day-21 assignment of Udemy's *100 Days of Code: The Complete Python Pro Bootcamp*: the classic Snake game, built in an object-oriented way with Python's `turtle` module. Day 21 teaches class inheritance and slicing and applies them to the game in five lectures: inheritance and slicing, detecting collisions with the food, the scoreboard, the wall, and the tail.

This repository continues the day-20 repository [020-snake-game], whose `main` already holds the finished game (food, score and game over included) with its tests, source documentation and review records. On 2026-10-08 S01 decided, in chat, to start this repository from that finished `main` and not to rebuild the game. The project therefore adopts the day-20 base, gives it the identity of this repository (name, links, description, README), and checks every behaviour against the day-21 lecture summaries, whose numbers the day-20 repository had to assume. The work is planned in three milestones, each delivered by one branch and one pull request. The game has no runtime dependencies.

## Methodological and Standards Foundation

- **Process:** the Software Quality Assurance (SQA) and Quality Criteria (QC)
  framework mounted at `framework/`: Business Case, Stakeholder Analysis,
  Project Plan, milestones, tasks synced as issues, then code, each step
  reviewed before the next. Analysis follows Larman, *Applying UML and
  Patterns*.
- **Quality model:** ISO/IEC 25010:2023; every QC criterion is tagged with a
  characteristic of it.
- **Code:** Python Enhancement Proposals (PEP) 8, 257 and 484, reviewed against `QC-PY-001`; comments in Doxygen style; tests with pytest.
- **Domain terms:** the lectures' own terms and names are used and recorded in the Domain Dictionary [DICT-001] (screen, snake, segment, head, body, tail, move, direction, reversal, food, refresh, eat, grow, score, scoreboard, wall, touch, game over, inheritance, and the names `create_snake`, `up`, `down`, `left`, `right`, `game_is_on`, `Food`, `Scoreboard`).

## Problem Statement

- The course shows the code only inside lecture videos, and the day-21 lectures change the same code several times (the food, the scoreboard, the wall, the tail). Nobody can run or compare the finished game without retyping it.
- A loose script cannot be run by someone else without guessing the Python version, the environment and the way to start it.
- A turtle program opens a window, so it is normally not tested, and mistakes in the rules (a snake that grows at the wrong place, a touch that is never detected) are found only by watching.
- The numbers of day 21 (size of the food, the distances of the two collisions, the wall) were assumptions in the day-20 repository, because it had only an outline of day 21. They have not yet been compared with the lecture summaries.
- A repository without description, topics or README is hard to find and hard to judge for the people who browse for ideas.

## Business Opportunity

A single finished, reproducible repository shows the whole path from lecture to documented, tested code. Starting from the finished base saves the rebuild, so the effort goes into what is new here: checking the game against the day-21 lectures and making the repository stand on its own. It can be compared with the solutions of other participants, shared, and reused as the pattern for the following days of the course.

## Objectives

| # | Objective |
| --- | --- |
| 1 | Keep the behaviour of the day-20 base: a 600 by 600 black window titled "My Snake Game"; a snake of three square segments at (0, 0), (-20, 0) and (-40, 0); a move of 20 pixels every 0.1 seconds; arrow keys that turn the head; and no reversal onto the snake |
| 2 | Deliver the food, eating, growth and score of the day-21 lectures: a blue circle of 10 by 10 pixels (half the size of a default turtle) at a random place inside the wall, so never at the very edge of the screen; the food is eaten when the head is closer than 15 pixels, moves to a new random place, makes the snake one segment longer, and raises the score on the scoreboard by 1 |
| 3 | Deliver the game over of the day-21 lectures: the game is over when the head passes the wall (280 pixels from the centre) or comes closer than 10 pixels to a segment of the tail; the text GAME OVER is shown in the middle of the window with the score still visible |
| 4 | Show the lessons of day 21 in the code: `Food` and `Scoreboard` inherit from `Turtle`, and the tail check loops over a slice of the segments that leaves out the head |
| 5 | Keep the assignment's structure and names: `Food` with `refresh`, `Scoreboard` with `increase_score`, `update_scoreboard` and `game_over`, `Snake` with `create_snake`, `add_segment`, `extend`, `move`, `up`, `down`, `left`, `right`, a `segments` list and a `head`, constants in `constants.py`, and a main flow that uses `screen`, `snake` and `game_is_on` |
| 6 | Provide a reproducible environment: Python 3.13 or newer, a local `.venv`, a `pyproject.toml`, and zero runtime dependencies |
| 7 | Prove the behaviour with pytest tests that need no display |
| 8 | Document the project: Doxygen comments in the source with a `Doxyfile`, and a README with set-up instructions for Windows PowerShell, Linux Debian and macOS |
| 9 | Keep every step traceable: one branch and one pull request per milestone, each pull request closing the issues it completes |
| 10 | Publish the repository with a description and topics |

## Scope

### In Scope

- Adopting the finished game of [020-snake-game] (source, tests, configuration, continuous integration workflow) as the base of this repository, and recording every difference from it.
- The five lectures of day 21: inheritance and slicing, detecting collisions with the food, the scoreboard, the wall, and the tail, as far as the lecture summaries give them.
- Checking each rule of the game against the lecture summaries, and correcting the base where it differs.
- Constants in `constants.py`; source in `src/`, tests in `tests/`, documents in `docs/`.
- `pyproject.toml`, Python `.gitignore`, `Doxyfile`, `README.md` following the Product Owner's template, a continuous integration (CI) workflow.
- Repository description and topics on the git host.

### Out of Scope

- Anything the lectures do not cover: sound, a menu, high-score storage between games (no lecture of day 21 stores one), restarting after game over, levels, configurable speed or window size.
- Rebuilding the game from the day-20 state; the finished base is used as it is.
- Keeping this repository and [020-snake-game] in step after today: a later fix in one of them is not carried to the other.
- Packaging for or publishing to the Python Package Index (PyPI).
- Runtime dependencies of any kind.
- Using or testing the tokens in `.env`; the file is for personal use only and is never imported by the project.

## Expected Benefits

### Tangible Benefits

- A finished game (day 21) that runs with one command after the README steps.
- A test suite that can run in continuous integration without a display.
- Generated source documentation.
- A repository page with description, topics and README.
- A written comparison of the game with the day-21 lectures, which the day-20 repository does not have.

### Intangible Benefits

- Practice with class inheritance, slicing and the `turtle` coordinate system, which is the aim of the lectures.
- A pattern for the following days of the course.
- Confidence from a step-by-step, reviewed delivery.

## Strategic Alignment

The project supports the participant's goal of finishing the bootcamp with repositories that other people can read, run and learn from, and it exercises the framework's rule that planning, review and code stay in step.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | The day-20 behaviour is kept | Window 600 by 600, black, titled "My Snake Game"; 3 segments at (0, 0), (-20, 0), (-40, 0); every move takes each segment 20 pixels and each segment takes the place of the one before it; the head turns to 90, 270, 180 and 0 degrees for up, down, left and right; a reversal is ignored | Manual run by S01 against the Go/No-Go list of [MIL-003], plus the matching tests |
| 2 | Food, eating and score follow the lectures | The food is a blue circle of 10 by 10 pixels at a random place inside the wall, so never at the very edge of the screen; when the head is closer than 15 pixels the food moves to a new random place, the snake grows by one segment at the place of its last segment and the score rises by 1 | Manual run by S01 against the Go/No-Go list of [MIL-003], plus the matching tests |
| 3 | Game over follows the lectures | The game ends when the head passes 280 pixels from the centre on any side or comes closer than 10 pixels to a segment behind the head; GAME OVER is shown in the middle with the score visible; the window closes on a click | Manual run by S01 against the Go/No-Go list of [MIL-003], plus the matching tests |
| 4 | The lessons of day 21 are visible | `Food` and `Scoreboard` are subclasses of `turtle.Turtle`; the tail check loops over `segments[1:]` | Review of `src/` |
| 5 | Tests are green and need no display | 100% of tests pass; 0 tests open a window; at least one test per public function and method of the logic modules | `pytest` exit code 0 locally and in CI |
| 6 | The set-up steps work | A fresh clone reaches a green `pytest` by following the README alone, on Windows PowerShell (by S01) and on Linux (by CI) | One run per operating system, recorded in the pull request |
| 7 | Source documentation builds | `doxygen Doxyfile` ends with 0 warnings | Doxygen output |
| 8 | No runtime dependencies | 0 entries in `[project].dependencies` | `pyproject.toml` |
| 9 | Names follow the assignment | 100% of the names listed in objective 5 exist with that spelling | Review of `src/` against objective 5 |
| 10 | Steps are traceable | 3 of 3 milestones merged by pull request, each description with one `Closes #N` line per completed issue | Pull request list and issue states |
| 11 | The repository page is complete | Non-empty description and at least 5 topics | Git host |
| 12 | The base is adopted without hidden change | Every difference between the adopted files and [020-snake-game] is listed in the pull request that introduces it | Pull request descriptions |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| `tkinter` is missing from the Python installation (typical on Debian) | The game cannot start | README lists `python3-tk` for Debian; the `snake` module does not import `turtle` at module level, so tests do not need it |
| Debian 12 ships Python 3.11, below the required 3.13 | Linux set-up fails | README states Debian 13 or newer, or a separately installed Python 3.13 |
| A turtle window cannot be opened in continuous integration | The tests cannot cover the game | `Snake` receives its segment factory as a parameter, so tests pass fakes; only `main` opens a window |
| The git host has no Actions runner | The continuous integration workflow is never executed | Provide the workflow file and run the same commands locally; recorded as an open issue of [PP-001] |
| Closing the window during the animation loop ends in a traceback (`_tkinter.TclError` or `turtle.Terminator`) | The game looks broken when it is quit | The adopted main flow exits quietly when the window is closed; [MIL-002] checks it |
| Author and reviewer are the same person (S01) | A defect can pass review unnoticed | Review against the QC checklists, record each review as an `RC-*`, and let the pull request be the second look |
| The lectures are available only as the summaries in the request | The game differs from the video | S01 compares the finished game with the video at the [MIL-003] Go/No-Go |
| The day-20 base was written against assumed day-21 numbers | A value of the base (size of the food, distances, range of the random place, text of game over) differs from the lectures | [MIL-003] checks each value against the lecture summaries and corrects the base where it differs |
| `Food` and `Scoreboard` inherit from `turtle.Turtle`, so importing them loads `turtle` and `tkinter` | A machine without `tkinter` cannot run the tests of these classes | The adopted tests install a fake `turtle` module before they import the classes |
| The random place of the food makes a test unreliable, or puts the food under the snake | A test fails now and then, or the game looks wrong | The random place comes from one function that the tests replace; whether the food may appear under the snake is an open issue of [PP-001] |
| The adopted files drift away from [020-snake-game] | A fix made in one repository is missing in the other | Out of scope by decision; each pull request lists the differences from the base |
| Tokens in `.env` leak into the repository | Credentials exposed | `.env` is in `.gitignore`, is never imported, and is not part of any task |

## Assumptions

- Python 3.13 or newer with `tkinter` is available on the machines that run the game.
- S01 is the only person who reviews and accepts artifacts.
- The git host is the Tirsvad Gitea instance, and its issues and milestones are used for tracking.
- The day-21 lecture summaries in the request are the specification of day 21; the video is the tie-breaker when a detail is missing.
- The finished `main` of [020-snake-game] is correct as far as its own tests and review records show, and is the base for every file that the milestones adopt.

## Constraints

- Python 3.13 or newer, in a virtual environment (`venv`).
- pytest for tests; `constants.py` for constants; `pyproject.toml` for project configuration; a Python `.gitignore`; Doxygen comments in the source and a `Doxyfile`.
- Folder structure `src/`, `tests/`, `docs/`.
- No runtime dependencies unless needed.
- Plan window from 2026-10-08 to 2026-10-16 (proposed, see [PP-001]), about one week of S01's spare time.
- Nothing is committed, pushed or merged without the Product Owner's request; changes are reviewed in the working tree first.
- The plan gate holds: no file under `src/` or `tests/` before an accepted, reviewed milestone that lists the task.

## Cost–Benefit Assessment

The assessment is qualitative on purpose: this is an unpaid learning project with one participant, so money does not measure either side.

| Costs | Benefits |
| --- | --- |
| About one week of S01's spare time, including reviews | A finished and shareable repository (objectives 1 to 10) |
| Review effort for the planning documents, which is large compared with the work left on the game | A traceable, repeatable way of working that later days can reuse |
| Two repositories that hold the same code and can drift apart | No rebuild of a game that already exists and is tested |
| Doxygen and pytest as development tools (not runtime) | Source documentation and automatic checks |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Wants a correct, tested and documented solution of the assignment: objectives 1 to 10 |
| S02 | Needs readable, runnable code with the assignment's names and README instructions (objectives 2, 3, 5, 6 and 8) |
| S03 | Needs a clear repository page and nothing to install (objectives 6, 8 and 10) |

## Recommendation

Proceed — the work left is small (adopt a finished and tested base, check it against the day-21 lectures, and publish it), the cost is about one week of the Product Owner's time, and the result is a reusable, documented repository.

---

[SA-001]: ./stakeholder-analysis.md
[DICT-001]: ./dictionary.md
[PP-001]: ./project-plan.md
[MIL-002]: ./milestones/mil-002-adopt-the-game.md
[MIL-003]: ./milestones/mil-003-check-against-day-21.md
[020-snake-game]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/020-snake-game
