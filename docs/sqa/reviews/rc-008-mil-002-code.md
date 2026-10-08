# RC-008: Review of the MIL-002 code

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-008 |
| CrossReference | [MIL-002], [QC-PY-001], [BC-001], [PP-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-08 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [0d3b913] |

---

## Artifact Under Review

- Instance reviewed: [MIL-002] tasks 1 to 5: `src/snake_game/snake.py`, `food.py`, `scoreboard.py`, `main.py`, `__main__.py` and the tests `tests/fakes.py`, `test_snake.py`, `test_food.py`, `test_scoreboard.py`, `test_main.py`
- Checklist used: [QC-PY-001]
- Scope: full review. `constants.py` and `test_constants.py` were reviewed in RC-007. The files are byte-identical to the base ([020-snake-game], commit `1a638c9`), checked with `cmp` for all ten files, so the review reads them as adopted code and does not ask for changes that the base does not have.
- Language and domain: n/a (technical type)
- Language reviewer: none

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Classes `Snake`, `Food`, `Scoreboard`, `Segment`, `ScreenLike`, `FoodLike`, `ScoreboardLike` in `PascalCase`; functions and methods in `snake_case`; constants in `UPPER_SNAKE`; the ruff `N` (pep8-naming) rules pass. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names are the lecture's and the dictionary's: `create_snake`, `add_segment`, `extend`, `hits_wall`, `hits_tail`, `refresh`, `increase_score`, `update_scoreboard`, `game_over`, `eat_food_if_close`, `end_game_if_over`, `game_is_on`. The same names appear in [DICT-001]. The only single-letter names are the parameters `x` and `y` of `goto` and `distance` in the `Segment` protocol, which mirror the `turtle` API (found with an AST search). |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff format --check src tests` reports 13 files already formatted; `ruff check src tests` reports all checks passed (rules E, F, W, I, N, UP, B, SIM); a search found no `noqa` and no `type: ignore`. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | `mypy` in strict mode reports no issues in 13 source files, which fails on an unannotated definition. Protocols (`Segment`, `ScreenLike`, `FoodLike`, `ScoreboardLike`) type the turtle objects so that the logic can take fakes. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | The only handler is `except (Terminator, TclError)` in `main.main`. It names two specific types, catches an external signal that the player closed the window, is explained in the docstring and in a comment, and a test covers the quiet exit. Nothing is raised, so there is no cause to keep. The convention warns against exceptions as normal control flow; here the window toolkit raises them, so S01 may want to confirm the decision. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | The only default argument is `segment_factory: ... | None = None`. An AST search for arguments, variables and definitions with a builtin's name found none in any module. |
| 7 | Files, locks and connections are managed with context managers | N-A | The modules open no file, lock or connection. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Every module, class, function and method has a Doxygen docstring or `##` comment; `doxygen Doxyfile` ends with 0 warnings (the Doxyfile fails the build on any warning). |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | A search found no `print` and no `logging` in `src`; the token values of `.env` occur in no tracked file. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | No Design Class Diagram exists in this project; the classes and operations trace to the day-21 lectures, to the base and to tasks 2 to 5 of [MIL-002]. The deviation is recorded in the Traceability section of [MIL-002]. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | `pytest` runs 128 tests (91 test functions, some parametrized), all green, none opens a window. The fake `turtle` and `tkinter` modules are installed with `monkeypatch.setitem`, which pytest undoes after each test. Each test file passes alone, and all files pass in reverse order. One test starts a fresh interpreter to prove that importing `main` loads no display module; it uses no network. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `strict = true`; `python -m mypy` ends with "Success: no issues found in 13 source files". `Any` occurs only as the return type of `make_food` and `make_scoreboard` in `tests/fakes.py`, each with a docstring that says why. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | No new dependency: the code uses the standard library only (`random`, `time`, `turtle`, `tkinter`, `typing`, `collections.abc`). The `dev` extra is as reviewed in RC-007. |

## Overall Verdict

Go — all Mandatory criteria pass; criterion 7 is N-A because no module opens a file, lock or connection. Commands run on 2026-10-08 in the `.venv` in Windows PowerShell: `pytest` (128 passed), `ruff check`, `ruff format --check`, `mypy`, `doxygen Doxyfile` (0 warnings). The assistant also started `python -m snake_game` twice and closed its window, once after about 2 seconds (during play) and once after about 5 seconds, by which time a snake moving right should have passed the wall: both ended with exit code 0 and an empty error output. The window title was "My Snake Game". The game-over text was not seen. That is a smoke test, not the manual play that [MIL-002] criterion 5 asks of S01. This review is **not independent**: the assistant that adopted the code also reviewed it, and author and reviewer (S01) are one person in a single-person project (risk recorded in [BC-001] and [PP-001]). S01 can overrule this verdict at the pull request.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Play the game in Windows PowerShell and confirm [MIL-002] criterion 5 (moves, turns, food, growth, score, wall, tail) | S01 | 2026-10-12 |
| Read the MIL-002 code and the list of differences from the base (none), and confirm or overrule this `Go` before the pull request is merged | S01 | 2026-10-12 |
| Confirm that catching `Terminator` and `TclError` to end quietly when the window is closed is acceptable (criterion 5) | S01 | 2026-10-12 |

---

[MIL-002]: ../../milestones/mil-002-adopt-the-game.md
[QC-PY-001]: ../../../framework/qc/qc-programming-python.md
[BC-001]: ../../business-case.md
[PP-001]: ../../project-plan.md
[020-snake-game]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/020-snake-game
[DICT-001]: ../../dictionary.md
[0d3b913]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/021-snake-game/commit/0d3b91321d2b88badbf51644a8b950159d1240c0
