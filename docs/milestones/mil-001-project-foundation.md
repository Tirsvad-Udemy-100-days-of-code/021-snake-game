# MIL-001: Project foundation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-08 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version, reviewed in RC-004 (Go) | [f13d004] |

---

## Purpose

This gate decides whether the repository is ready to hold the game: a fresh clone can be set up from the README, the tests and the documentation build run, every constant of the game lives in one module, and the repository page says what the project is. The files are adopted from the base ([020-snake-game], `main`) and given the identity of this repository. The work is delivered on the branch `mil-001-project-foundation` and one pull request.

## Deliverable

The repository files that carry no game logic yet: `pyproject.toml`, the Python `.gitignore`, the package `src/snake_game/` with `constants.py`, `tests/test_constants.py`, `README.md` following the Product Owner's template, `Doxyfile`, and the continuous integration workflow `.gitea/workflows/ci.yml`. The repository description and topics on the git host are set.

Each adopted file is copied from the base and changed only where the identity of this repository requires it (project name, description, repository links, day number). The pull request lists every difference from the base.

Proposed repository description and topics, for S01 to confirm before they are set:

- Description: "Snake game in Python with turtle graphics and object-oriented design: the snake eats food, grows, keeps a score and ends at the wall or at its own tail. Day 21 of Udemy's 100 Days of Code Python bootcamp, with pytest tests and Doxygen docs. No runtime dependencies."
- Topics: `100-days-of-code`, `doxygen`, `education`, `game`, `oop`, `pytest`, `python`, `python-bootcamp`, `python3`, `snake-game`, `turtle-graphics`, `udemy`.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | In a fresh clone, `python -m venv .venv`, `python -m pip install --upgrade pip` and `python -m pip install -e ".[dev]"` succeed in Windows PowerShell | All three commands exit 0 | Any command fails |
| 2 | `pytest` runs | Exit code 0, at least one test of `constants.py`, no window opened | Failing test, or no test of `constants.py` |
| 3 | `pyproject.toml` states the Python version and the dependencies | `requires-python = ">=3.13"`, `dependencies = []`, a `dev` extra with pytest, and a repository URL that names this repository | Any of the four is missing or different |
| 4 | The `.gitignore` protects local files | `git check-ignore .venv .env __pycache__` lists all three | One of them is not ignored |
| 5 | `constants.py` holds the values of the lectures | Screen width, height, colour and title; segment shape and colour; the three starting positions; the move distance; the four directions; the refresh delay; the food shape, size, colour and speed; the wall; the eating distance; the scoreboard label, colour, position, alignment and font; the touch distance; the game-over text and place are constants with Doxygen comments | A value of the list is missing or has no Doxygen comment |
| 6 | `doxygen Doxyfile` builds the source documentation | Ends with 0 warnings and writes HTML for `src/` | Any warning, or no output |
| 7 | The README follows the Product Owner's template | Every section title of the template in the given order, with commands for Windows PowerShell, Linux Debian and macOS | A heading is missing, out of order, or a section has no commands |
| 8 | The continuous integration (CI) workflow exists | `.gitea/workflows/ci.yml` installs `.[dev]` and runs `pytest`, `ruff` and `mypy` on Python 3.13, and nothing under `.github/workflows` exists | No workflow, or it does not run the tests, or a file exists under `.github/workflows` |
| 9 | The repository page is complete | Description is non-empty and there are at least 5 topics on the git host | Description empty or fewer than 5 topics |
| 10 | The adopted files are traceable to the base | The pull request lists every difference between each adopted file and the base, or says that there is none | A difference that the list does not name |
| 11 | The code is reviewed | `RC-*` against `QC-PY-001` has the verdict `Go` | Verdict `No-Go` or `Go-with-conditions` |
| 12 | No secret is in the change | `.env` is not tracked and no token appears in any changed file | A token is found in the diff |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [PP-001] accepted | The plan schedules this gateway; the plan-first gate needs it before any code |
| This milestone accepted with a `Go` review | The plan-first gate allows no file under `src/` or `tests/` before that |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 6: reproducible environment, no runtime dependencies | [BC-001], criteria 6 and 8 in Success Criteria |
| Objective 7: tests without a display | [BC-001], criterion 5 in Success Criteria |
| Objective 8: Doxygen and README | [BC-001], criteria 6 and 7 in Success Criteria |
| Objective 10: repository page | [BC-001], criterion 11 in Success Criteria |
| Objective 9: traceable steps; the base is adopted without hidden change | [BC-001], criteria 10 and 12 in Success Criteria |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-09 — first of three gateways, inside the one-week plan of [PP-001] that ends 2026-10-16.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add pyproject.toml for the Day 21 repository | Adopt `pyproject.toml` from the base for the `snake-game` project: `requires-python = ">=3.13"`, an empty `dependencies` list, an optional `dev` extra with pytest, ruff and mypy, the `src` layout for the package `snake_game`, the pytest settings (`testpaths = ["tests"]`), and a description and repository URL that name this repository and day 21. Serves objective 6 of the Business Case: a reproducible environment without runtime dependencies. | No | |
| 2 | Add the Python .gitignore for the Day 21 repository | Adopt the Python `.gitignore` from the base: bytecode, `.venv/`, build and packaging output, pytest, ruff, mypy and Doxygen output. It also ignores `.env`, so the personal tokens can never be committed or become part of the project. | No | |
| 3 | Adopt constants.py and its test | Copy `src/snake_game/__init__.py`, `src/snake_game/constants.py` and `tests/test_constants.py` from the base. The constants hold every value of the lectures as `UPPER_SNAKE` constants with Doxygen comments, the day-21 values included (food, wall, eating distance, scoreboard, touch distance, game-over text). Values that the day-21 lecture summaries fix differently are corrected in MIL-003, not here. | No | |
| 4 | Add the README for the Day 21 repository | Adopt `README.md` from the base and rewrite its identity for this repository (name, day 21, clone address). Keep the Product Owner's template (Requirements, Set up for Windows PowerShell, Linux Debian and macOS, Run, Run the tests, Continuous integration, Build the source documentation, Project layout, License). Document creating a local `.venv`, `python -m pip install --upgrade pip` and `python -m pip install -e ".[dev]"`; name `python3-tk` and Debian 13 for Linux. The Run section is finished in MIL-003. Serves S02 and S03. | No | |
| 5 | Add the Doxyfile for the Day 21 repository | Adopt the `Doxyfile` from the base: it reads `src/`, writes to `build/doxygen`, extracts documentation for Python (Doxygen comment style, `OPTIMIZE_OUTPUT_JAVA`) and treats warnings as failures; the project brief names day 21. The README documents the command `doxygen Doxyfile`. | No | |
| 6 | Add the continuous integration workflow | Adopt `.gitea/workflows/ci.yml` (run by Gitea Actions) from the base: check out, set up Python 3.13, `python -m pip install --upgrade pip`, `python -m pip install -e ".[dev]"`, run `pytest`, `ruff` and `mypy`. The tests need no display. The file stays in `.gitea/workflows`, not `.github/workflows`, because GitHub refuses a push that touches `.github/workflows` from a token without the workflow scope, which would block the push mirror to GitHub. | No | |
| 7 | Set the repository description and topics | Set the description and at least 5 topics of this repository on the git host with the Gitea application programming interface (API), using `GITEA_TOKEN` from the personal `.env` file; the file is only read by the command, never imported, tested or tracked. Use the proposed text of the Deliverable section once S01 has confirmed it. Serves S03 and objective 10 of the Business Case. | No | |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[020-snake-game]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/020-snake-game
[f13d004]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/021-snake-game/commit/f13d004447ceb631cb22c058d68a21b721a3f04c
