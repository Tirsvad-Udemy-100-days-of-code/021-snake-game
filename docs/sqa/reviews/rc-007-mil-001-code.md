# RC-007: Review of the MIL-001 code

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-007 |
| CrossReference | [MIL-001], [QC-PY-001], [BC-001], [PP-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-08 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [MIL-001] task 3 and the code of tasks 1 to 6: `src/snake_game/__init__.py`, `src/snake_game/constants.py` and `tests/test_constants.py` (the Python source of the milestone)
- Checklist used: [QC-PY-001]
- Scope: full review. The non-Python files of the milestone (`pyproject.toml`, `.gitignore`, `Doxyfile`, `README.md`, `.gitea/workflows/ci.yml`) are not Python source; the Go/No-Go criteria of [MIL-001] check them.
- Language and domain: n/a (technical type)
- Language reviewer: none

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Package `snake_game`, module `constants`, constants in `UPPER_SNAKE`, test functions in `snake_case`; the ruff rule set includes the `N` (pep8-naming) rules and passes. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Constants carry the dictionary terms (`MOVE_DISTANCE`, `WALL_LIMIT`, `FOOD_COLLISION_DISTANCE`, `GAME_OVER_TEXT`). The only short names are `x`, `y`, `left` and `right` inside one-line comprehensions and unpackings of the tests. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff format --check src tests` reports 3 files already formatted; `ruff check src tests` reports all checks passed (rules E, F, W, I, N, UP, B, SIM); a search found no `noqa` and no `type: ignore`. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | All 21 test functions are annotated `-> None`; every constant is annotated `Final[...]`; `mypy` in strict mode reports no issues in 3 source files. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | N-A | The files contain no exception handling (a search for `except` found nothing). |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No function has a default argument; no builtin name is used as a name. |
| 7 | Files, locks and connections are managed with context managers | N-A | The files open no file, lock or connection. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | `__init__.py` and `constants.py` have a module docstring and a Doxygen file comment; every constant has a Doxygen `##` comment; `doxygen Doxyfile` ends with 0 warnings. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No `print` and no logging in the files; the values of `GITEA_TOKEN` and `GITHUB_PAT` occur only in the untracked, ignored `.env` file (searched by value, names only). |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | This milestone defines no class or operation, only constants, which trace to the lecture values listed in the Deliverable of [MIL-001]. The classes of the game arrive in MIL-002, which records the deviation (no Design Class Diagram exists). |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | `tests/test_constants.py` has 21 tests named for a behaviour (for example `test_wall_is_280_pixels_from_the_centre`); `pytest` ran 21 tests (21 passed, none opens a window); the tests read module constants only, so they share no state and use no network. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `[tool.mypy] strict = true`; `python -m mypy` ends with "Success: no issues found in 3 source files"; the files do not use `Any`. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | `dependencies = []`; the `dev` extra declares pytest, ruff and mypy with lower bounds (`>=`), and all three are used by the checks above. They are not pinned to exact versions, which this Optional criterion would ask for; it is accepted for a development-only extra. |

## Overall Verdict

Go — all Mandatory criteria pass or are N-A with a reason (criteria 5, 7 and 10 do not apply to a module of constants). Commands run on 2026-10-08 in a fresh `.venv` in Windows PowerShell: `pytest` (21 passed), `ruff check`, `ruff format --check`, `mypy`, `doxygen Doxyfile` (0 warnings). The files are copies of the base ([020-snake-game]) with identity-only edits (day number in docstrings, description and repository URL in `pyproject.toml`). This review is **not independent**: the assistant that adopted the code also reviewed it, and author and reviewer (S01) are one person in a single-person project (risk recorded in [BC-001] and [PP-001]). S01 can overrule this verdict at the pull request.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Read the MIL-001 code and the list of differences from the base, and confirm or overrule this `Go` before the pull request of MIL-001 is merged | S01 | 2026-10-09 |

---

[MIL-001]: ../../milestones/mil-001-project-foundation.md
[QC-PY-001]: ../../../framework/qc/qc-programming-python.md
[BC-001]: ../../business-case.md
[PP-001]: ../../project-plan.md
[020-snake-game]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/020-snake-game
