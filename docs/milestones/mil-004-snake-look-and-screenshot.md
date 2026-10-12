# MIL-004: Snake look and screenshot

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [7d5bc3e] |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | The wiki is published in three languages (English, Danish, Bahasa Melayu) after S01's request in chat; Deliverable, Go/No-Go criterion 12 and task 9 changed | [7d5bc3e] |

---

## Purpose

This gate decides whether the snake looks as S01 asked for on 2026-10-13 (a light green body and a dark green head with a mouth at its front), and whether the README and the wiki show the finished game in a real screenshot at a score of 5. Nothing else about the game changes. The look is a deliberate change from the white squares of the lectures, recorded as objective 11 of [BC-001]; the screenshot is objective 12. It is the fourth gate of [PP-001], added on 2026-10-13 after [MIL-003] was merged. The work is delivered on the branch `mil-004-snake-look-and-screenshot` and one pull request; the wiki pages are files in the folder `wiki/` of the same pull request and are published to the wiki by the instance's workflow when it is merged.

## Deliverable

The colours and the shape of the head in `src/snake_game/constants.py` (`SEGMENT_COLOR` is replaced by `BODY_COLOR`), the building and registering of the head shape in `src/snake_game/main.py`, the use of the head shape and the two colours in `src/snake_game/snake.py`, the tests for each, the README sections that describe the look, the screenshot `docs/images/snake-score-5.png` shown in the README, the folder `wiki/` with the wiki pages in three languages (English, Danish and Bahasa Melayu), whose home pages show the same screenshot, and the framework pin brought to the version the working tree holds. Running the game shows a light green body and a dark green head with a mouth that turns with the head.

The request gave the look in one line ("body light green, head dark green, head with mouth"), so the exact greens and the shape of the mouth below are **assumptions**. They are listed here so that S01 can confirm or replace each of them when accepting the plan, before any code is written (Go/No-Go criterion 1). The shape is given as numbers in turtle shape coordinates, in which the front of the head is the positive y direction and the head is 20 by 20 pixels, so that S01 can change a number and not a picture.

| Value | Assumed | Constant |
| --- | --- | --- |
| Colour of the body segments | light green (Tk colour `light green`, #90EE90) | `BODY_COLOR` |
| Colour of the head | dark green (Tk colour `dark green`, #006400) | `HEAD_COLOR` |
| Shape of a body segment | the 20 by 20 pixel square of the lectures | `SEGMENT_SHAPE` (unchanged) |
| Shape of the head | the same square: corners (-10, -10), (-10, 10), (10, 10), (10, -10) | `HEAD_SHAPE` (the name), `HEAD_OUTLINE` |
| The mouth | a wedge cut into the middle of the front edge: points (-6, 10), (0, 2), (6, 10), that is 12 pixels wide at the edge and 8 pixels deep | `MOUTH_OUTLINE` |
| Colour of the mouth | black, the colour of the background, so it looks cut out | `MOUTH_COLOR` |
| Direction of the mouth | at the front of the head: right at the start, then up, left or down with the head | none (part of the shape) |
| Movement of the mouth | none; it does not open or close | none |
| Food, scoreboard, GAME OVER text | unchanged | none |

The screenshot has these properties:

| Property | Value |
| --- | --- |
| File | `docs/images/snake-score-5.png`, PNG |
| What it shows | The window of the running game (`python -m snake_game`) with its title bar, at the moment the scoreboard of that window reads `Score: 5`: a light green body of seven segments, a dark green head with its mouth, the blue food, the white score |
| How it is made | The real game is run and played; the food is moved in front of the head to reach the score of 5 quickly, which is the only help; the window is captured with the operating system's own window capture and saved as PNG. It is not a drawing. The script that does this is a one-off and is not part of the repository |
| Where it is used | The README (below the introduction and in the Run section) and the home pages `Home`, `Home.da` and `Home.ms` of the wiki of the repository, which refer to the file on `main` |

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The assumed values are confirmed | S01 accepted the plan that lists the values of the first table in the Deliverable section, or replaced any of them in chat, and the pull request lists the final values | A value is unconfirmed or missing from the pull request |
| 2 | The body is light green | A run of the game shows every segment behind the head as a light green square, and a segment gained by eating is light green too | A white or other coloured segment |
| 3 | The head is dark green with a mouth | The head is a dark green square with a wedge cut into the middle of its front edge in the colour of the background | A white head, no mouth, or a mouth that is not at the front |
| 4 | The mouth turns with the head | After Up, Left and Down the mouth is at the front of the head each time | The mouth stays on one side |
| 5 | The rest looks and behaves as before | The food is still a blue circle, the score and GAME OVER are still white text, and the snake moves, eats, grows and ends the game as before | Any of those changed |
| 6 | Constants are in one place | Every value of the first table is a constant with a Doxygen comment and no other module defines it; `SEGMENT_COLOR` no longer exists | A value is a literal in another module, or `SEGMENT_COLOR` is still used |
| 7 | Earlier behaviour is unchanged | The tests of [MIL-001] to [MIL-003] still pass, except those that name the old white colour, which are changed on purpose | A regression |
| 8 | Tests prove the behaviour | `pytest` exits 0 with no display; tests cover the head shape built from the constants (two components), its registration once under `HEAD_SHAPE`, the shape and colour of the head and of a body segment, and that `extend` adds a light green segment, using fakes only; importing `main` loads neither `turtle` nor `tkinter` | A failing test, or one of those behaviours has no test |
| 9 | The checks are green | `ruff check src tests`, `ruff format --check src tests` and `mypy` exit 0, `doxygen Doxyfile` ends with 0 warnings, and the CI run of the pull request is green | Any check fails |
| 10 | The screenshot is real | `docs/images/snake-score-5.png` is a PNG of the window of the running game, captured when the scoreboard of that window read `Score: 5`; the pull request states the score read from the window at that moment and the pixel counts of the five colours of the game (black, light green, dark green, blue, white) | The file is a drawing, shows another score, or lacks one of the five colours |
| 11 | The README shows and describes the look | It says light green body and dark green head with a mouth that turns with the head, shows the screenshot with alt text and a caption that names the score, and no sentence calls the segments white | An out-of-date sentence, or no screenshot |
| 12 | The wiki shows the game in three languages | The wiki of the repository has the pages `Home` (English), `Home.da` (Danish) and `Home.ms` (Bahasa Melayu), each with a short description of the game, its controls and the screenshot, whose address is the file on `main`, and a `_Sidebar` page that lists the three languages and the marker `wiki/.publish`, all files of the folder `wiki/` as the wiki of `TirSystem/github-action` does; every page links to the other two; the address of the screenshot answers HTTP 200 with an image | A language is missing, a page does not link to the other two, or a screenshot that does not load |
| 13 | The framework pin and the review links agree | The superproject records the commit that the working tree of `framework/` holds, and every link to a QC checklist in RC-001 to RC-008 resolves to an existing file | A link that does not resolve |
| 14 | The code is reviewed | `RC-*` against `QC-PY-001` has the verdict `Go` | Verdict `No-Go` or `Go-with-conditions` |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-003] accepted and merged | The whole game, its constants and its tests are on `main` there; the look changes them and the screenshot shows them |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 11: light green body, dark green head with a mouth | [BC-001], criterion 13 in Success Criteria |
| Objective 12: a real screenshot in the README and on the wiki | [BC-001], criterion 14 in Success Criteria |
| Objective 1: the day-20 behaviour is kept | [BC-001], criterion 1 in Success Criteria |
| Objective 5: the assignment's names (`Snake`, `head`, `segments` stay) | [BC-001], criterion 9 in Success Criteria |
| Objective 7: tests without a display | [BC-001], criterion 5 in Success Criteria |
| Objective 8: Doxygen and README | [BC-001], criteria 6 and 7 in Success Criteria |
| Objective 9: traceable steps | [BC-001], criterion 10 in Success Criteria |
| Design of the head shape and the two colours: no Design Class Diagram exists; they trace to S01's request of 2026-10-13 and to tasks 2 to 4 below, a recorded deviation from `QC-PY-001` criterion 10 as in [MIL-002] | [PP-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-15 — the fourth and last gateway, added to the plan of [PP-001] on 2026-10-13; it uses the first of the two buffer days, so the end date 2026-10-16 in the Constraints of [BC-001] does not move.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Bring the framework pin to the version of the working tree | Record the `framework` submodule at the commit its working tree already holds (v0.6.2 plus two later commits of the framework's `main`; the recorded commit is v0.4.0) as a commit of its own, and repoint the 14 link definitions in RC-001 to RC-008 from `framework/qc/qc-*.md` to `framework/qc/artifacts/` and `framework/qc/code/`, where the QC checklists now are, so that every link resolves again. The installed skills, agents and rules already equal the framework's (compared with `diff`; they are not tracked by git), so nothing is reinstalled. Nothing under `src/` or `tests/` changes. | No | |
| 2 | Add the snake colour and head constants | In `src/snake_game/constants.py` replace `SEGMENT_COLOR` by `BODY_COLOR` (light green) and add `HEAD_COLOR` (dark green), `HEAD_SHAPE` (the name under which the head shape is registered), `HEAD_OUTLINE`, `MOUTH_OUTLINE` and `MOUTH_COLOR`, each with a Doxygen comment, and update `tests/test_constants.py` (the head is the 20 by 20 square, the mouth lies on its front edge and inside it, the head and the body differ in colour). Start only after the values are confirmed (Go/No-Go criterion 1). | No | |
| 3 | Build and register the head shape with a mouth | In `src/snake_game/main.py` add `register_head_shape(screen)`, which builds a compound `turtle.Shape` of two components (the head outline in `HEAD_COLOR` and the mouth in `MOUTH_COLOR`) and registers it under `HEAD_SHAPE`; `main` calls it once before the snake is made. `turtle.Shape` is imported inside the function so that importing `main` still needs neither `turtle` nor `tkinter`, and `ScreenLike` gains `register_shape`. | No | |
| 4 | Colour the body light green and the head dark green | In `src/snake_game/snake.py` the first segment gets the shape `HEAD_SHAPE`, whose colours are inside the shape, and every other segment, a new one made by `extend` too, gets `SEGMENT_SHAPE` and `BODY_COLOR`. The head stays `segments[0]` and `head`, so the lectures' names do not change. | No | |
| 5 | Test the snake colours and the head shape without a display | Extend the fakes with a fake `turtle.Shape` that records `addcomponent`, and test: the head shape has two components built from the constants, it is registered once under `HEAD_SHAPE`, the head has that shape, a body segment has `SEGMENT_SHAPE` and `BODY_COLOR`, `extend` adds a light green segment, the pen is still lifted before a segment moves, and importing `main` loads neither `turtle` nor `tkinter`. Change the earlier tests that name white. | No | |
| 6 | Describe the snake's look in the README | Say in the Run section and the introduction of `README.md` that the body is light green and the head dark green with a mouth, and remove the sentences that call the segments white. Confirm that `doxygen Doxyfile` ends with 0 warnings. | No | |
| 7 | Capture the game window at a score of 5 as a screenshot | After tasks 2 to 5 are on the branch, run the real game (`python -m snake_game`) in a window, steer it with key events, move the food in front of the head until the scoreboard reads `Score: 5`, and capture that window with the operating system's window capture. Save it as `docs/images/snake-score-5.png`. Write in the pull request the score read from the window and the pixel counts of black, light green, dark green, blue and white. The capture script is a one-off outside the repository. | No | |
| 8 | Show the screenshot in the README | Add the screenshot to `README.md` below the introduction and in the Run section, with alt text and a caption that says it is the game at a score of 5 with a light green body and a dark green head with a mouth. | No | |
| 9 | Write the wiki pages in three languages | In the repository folder `wiki/`, as the wiki of `TirSystem/github-action` does, write `Home.md` (English), `Home.da.md` (Danish, Dansk) and `Home.ms.md` (Bahasa Melayu), each with a short description of the game, its controls, how to run it and the screenshot, which refers to `docs/images/snake-score-5.png` on `main`, and a language switch `English \| Dansk \| Bahasa Melayu` at the top; add `_Sidebar.md` that lists the three languages. The empty marker `wiki/.publish` makes the instance's scoped workflow Publish wiki copy them to the wiki of the repository when a pull request is merged to `main`; it needs the secret `TOKEN_FOR_GITEA_WIKI` of the organization. That secret is missing in the organization `Tirsvad-Udemy-100-days-of-code` (checked on 2026-10-13), so the marker is **not** in this pull request: it is added by S01 together with the secret, and until then the pages are in the repository only (a token is never printed or typed). The pages are part of the pull request, which says `Closes` for this task. | No | |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-001]: ./mil-001-project-foundation.md
[MIL-002]: ./mil-002-adopt-the-game.md
[MIL-003]: ./mil-003-check-against-day-21.md
[7d5bc3e]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/021-snake-game/commit/7d5bc3e2bc6f9e2e515b1aa3212a2d9f240f48f2
