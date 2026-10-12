# RC-013: Review of the MIL-004 code

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-013 |
| CrossReference | [MIL-004], [QC-PY-001], [BC-001], [PP-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [7d5bc3e] |

---

## Artifact Under Review

- Instance reviewed: [MIL-004] tasks 2 to 5: `src/snake_game/constants.py`, `main.py` (`register_head_shape`), `snake.py` and the tests `tests/fakes.py`, `test_constants.py`, `test_snake.py`, `test_main.py`
- Checklist used: [QC-PY-001]
- Scope: full review of the changed files (a diff of 9 files against `main`; `food.py`, `scoreboard.py` and their tests are unchanged)
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (the code was written by the `python-developer` agent of this session and reviewed by the assistant that delegated it, as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing | Pass | `register_head_shape` in `snake_case`; `BODY_COLOR`, `HEAD_COLOR`, `HEAD_SHAPE`, `HEAD_OUTLINE`, `MOUTH_OUTLINE`, `MOUTH_COLOR` in `UPPER_SNAKE`; ruff `N` rules pass. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations | Pass | The names are those of the Dictionary row `mouth` and of the request (body, head, mouth). |
| 3 | Formatter and linter pass with no unexplained suppressions | Pass | `ruff format --check src tests` and `ruff check src tests` exit 0; no `noqa`, no `type: ignore`. |
| 4 | Every signature is type-annotated, including `-> None` | Pass | `mypy` strict ends with no issues in 13 source files. The `Shape` annotation of `ScreenLike.register_shape` is imported under `TYPE_CHECKING`, so nothing extra is imported at run time. |
| 5 | No bare `except:`, no swallowed exceptions | Pass | No handler was added. |
| 6 | No mutable default arguments, no shadowed builtins | Pass | The new code has none. |
| 7 | Files, locks and connections use context managers | N-A | The change opens none. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Every new constant has a `##` comment and `register_head_shape` a Doxygen docstring; `doxygen Doxyfile` ends with 0 warnings. |
| 9 | Logging uses `logging`, not `print`; no secrets in output | Pass | No `print` or `logging` was added. |
| 10 | Classes and operations trace to the Design Class Diagram | Pass | None exists; the look traces to S01's request of 2026-10-13 and to tasks 2 to 4 of [MIL-004]; the deviation is recorded in its Traceability section. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | `pytest` runs 138 tests, all green, none opens a window; the head shape (two components from the constants), its single registration before `Snake()` is made, the head and body shape and colour and a light green segment from `extend` are tested; importing `main` still loads neither `turtle` nor `tkinter`. |
| 12 | Type checker runs in strict mode without errors | Pass | `mypy` strict: no issues. |
| 13 | Dependencies are declared, none unused | Pass | No dependency was added; the screenshot script that uses Pillow is a one-off outside the repository. |
| 14 | Each piece of knowledge is defined in one place | Pass | The two greens, the head outline, the mouth and its colour are defined only in `constants.py`; `SEGMENT_COLOR` no longer exists (a search found no use). |
| 15 | Imports point inward | Pass | `snake.py` imports only constants; `main.py` imports `turtle` inside the function. |
| 16 | SOLID holds | Pass | The head's look is a registered shape chosen by name, so `Snake` does not know how it is drawn; the colour choice lives in `add_segment`. |

## Overall Verdict

Go — all Mandatory criteria pass; criterion 7 is N-A. Commands run on 2026-10-13: `pytest` (138 passed), `ruff check`, `ruff format --check`, `mypy`, `doxygen Doxyfile` (0 warnings). The mouth direction was checked with a real turtle: at heading 0 and 90 the point (0, 2) is at the front of the head. The game was played with a one-off script and its window captured at a score of 5 (`docs/images/snake-score-5.png`). This review is **not independent**: the assistant that delegated the code also reviewed it, and author and reviewer (S01) are one person in a single-person project. S01 can overrule this verdict at the pull request.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Play the game, look at the colours and the mouth, and say in the pull request if a value should change | S01 | 2026-10-15 |

---

[MIL-004]: ../../milestones/mil-004-snake-look-and-screenshot.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[BC-001]: ../../business-case.md
[PP-001]: ../../project-plan.md
[7d5bc3e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/021-snake-game/commit/7d5bc3e2bc6f9e2e515b1aa3212a2d9f240f48f2
