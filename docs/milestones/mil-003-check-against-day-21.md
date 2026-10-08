# MIL-003: Check against day 21

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-08 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version, reviewed in RC-006 (Go) | pending |

---

## Purpose

This gate decides whether the adopted game does what the five day-21 lectures say, and whether the repository is finished. The base was written against assumed day-21 numbers; this milestone replaces the assumptions by the values of the lecture summaries, corrects the code where it differs, and finishes the README. It is the last gate of [PP-001]. The work is delivered on the branch `mil-003-check-against-day-21` and one pull request.

## Deliverable

A comparison table in the pull request with one row per lecture point below (value in the lecture summary, value in the code, same or different), the corrections of every difference with tests, a finished `README.md` that describes the whole game and this repository, and a check of the repository page. If nothing differs, the table says so and no source file changes.

The lecture points are the specification of this milestone:

| Lecture | Point of the lecture summary | Where it lives in the code |
| --- | --- | --- |
| 1. Inheritance and slicing | One class inherits the attributes and methods of another; lists are sliced | `class Food(Turtle)`, `class Scoreboard(Turtle)`, `segments[1:]` |
| 2. Detect collisions with food | `Food` inherits from `Turtle`; a blue circle of 10 by 10 pixels | `FOOD_SHAPE`, `FOOD_COLOR`, `FOOD_SIZE` (0.5 of a default turtle) |
| 2. Detect collisions with food | The random place comes from the `random` module and is never at the edge of the screen | `random_coordinate`, `WALL_LIMIT` (280) |
| 2. Detect collisions with food | The snake eats the food when the distance between the head and the food is less than 15 pixels | `FOOD_COLLISION_DISTANCE`, `eat_food_if_close` |
| 2. Detect collisions with food | `refresh` gives the food new random coordinates; it runs when the food is made and at every collision | `Food.refresh`, called from `Food.__init__` and `eat_food_if_close` |
| 3. Scoreboard | `Scoreboard` inherits from `Turtle`; the score starts at 0; the text is written with alignment and font; the turtle is hidden; colour and place are set | `Scoreboard.__init__`, `SCOREBOARD_COLOR`, `SCOREBOARD_POSITION`, `SCOREBOARD_ALIGNMENT`, `SCOREBOARD_FONT` |
| 3. Scoreboard | `increase_score` adds 1; the old text is cleared before the new text is written; `update_scoreboard` does both; alignment and font are constants | `Scoreboard.increase_score`, `Scoreboard.update_scoreboard` |
| 4. Wall | The wall is at 280 and -280 on both axes; passing it stops the game (`game_is_on` becomes false); GAME OVER is shown in the middle with the score still visible | `Snake.hits_wall`, `WALL_LIMIT`, `Scoreboard.game_over`, `GAME_OVER_TEXT`, `GAME_OVER_POSITION` |
| 5. Tail | Eating adds a segment: `extend` calls `add_segment` with the position of the last segment | `Snake.extend`, `Snake.add_segment` |
| 5. Tail | The head touches the tail when it is closer than 10 pixels to a segment; the head is skipped, so it does not collide with itself | `Snake.hits_tail`, `TAIL_COLLISION_DISTANCE`, `segments[1:]` |

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The comparison is complete | The pull request has one row for every lecture point above, with the value of the lecture summary, the value of the code and the result | A lecture point has no row |
| 2 | Every difference is resolved | Each row marked different is corrected in the code with a test, or S01 accepts it with a reason written in the pull request | A difference stays open |
| 3 | The lessons of day 21 are visible | `Food` and `Scoreboard` are subclasses of `turtle.Turtle` and call `super().__init__()`; `hits_tail` loops over `segments[1:]` | Either class does not inherit from `Turtle`, or the loop includes the head |
| 4 | Food is shown | A manual run shows one small blue circle at a random place inside the wall; a second run shows another place; it is never at the very edge of the screen | No food, not a circle, or outside the wall |
| 5 | The snake eats | When the head comes closer than `FOOD_COLLISION_DISTANCE` the food moves to a new random place, the snake grows by one segment and the score rises by 1; it works again for the next food | Any of the three does not happen, or the score rises without the food being eaten |
| 6 | The scoreboard shows the score | White text `Score: 0` at the top centre; after eating it shows `Score: 1` and the old text is gone | Text overlaps, is missing or is not at the top centre |
| 7 | The wall ends the game | A manual run shows the game ending when the head passes the wall on each of the four sides; GAME OVER is in the middle of the window and the score stays visible | The game goes on beyond the wall, ends inside it, or shows no text |
| 8 | The tail ends the game | Turning the head into the body ends the game; normal movement, including the moves right after eating, does not | The game does not end, or ends without a touch |
| 9 | A click closes the window | After game over a click closes the window and the program ends with exit code 0; closing the window during play also ends with exit code 0 and no traceback | The window stays, or a traceback appears |
| 10 | Tests and checks are green | `pytest` exits 0 with no display; `ruff check`, `ruff format --check` and `mypy` exit 0; `doxygen Doxyfile` ends with 0 warnings | Any check fails |
| 11 | The README is finished | It describes the whole game (moving, food, score, game over, closing) and this repository; it has no placeholder and no sentence that is out of date; a fresh clone reaches a green `pytest` by following it | A placeholder or an out-of-date sentence, or a command fails |
| 12 | The repository page is complete | Description is non-empty and there are at least 5 topics on the git host | Description empty or fewer than 5 topics |
| 13 | The game matches the lecture | S01 compares the finished game with the lecture video and notes any difference in the pull request | An undocumented difference |
| 14 | The code is reviewed | If a source file changed, `RC-*` against `QC-PY-001` has the verdict `Go`; if none changed, the pull request says so | Verdict `No-Go` or `Go-with-conditions` |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-002] accepted and merged | The game that is checked exists there |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 2 and 3: food, eating, score, game over as the lectures give them | [BC-001], criteria 2 and 3 in Success Criteria |
| Objective 4: inheritance and slicing | [BC-001], criterion 4 in Success Criteria |
| Objective 1: the day-20 behaviour is kept | [BC-001], criterion 1 in Success Criteria |
| Objective 7: tests without a display | [BC-001], criterion 5 in Success Criteria |
| Objective 8: README and Doxygen | [BC-001], criteria 6 and 7 in Success Criteria |
| Objective 9: traceable steps | [BC-001], criterion 10 in Success Criteria |
| Objective 10: repository page | [BC-001], criterion 11 in Success Criteria |
| Design of any corrected class or method: no Design Class Diagram exists; a correction traces to its lecture point in the table above, a recorded deviation from `QC-PY-001` criterion 10 as in [MIL-002] | [PP-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-14 — last of three gateways, inside the one-week plan of [PP-001] that ends 2026-10-16.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Check inheritance and slicing against lecture 1 | Compare the code with the lecture on class inheritance and slicing: `Food` and `Scoreboard` are subclasses of `Turtle` that call `super().__init__()`, and the tail check slices the segments so that the head is left out. Write the result as rows of the comparison table in the pull request. | No | |
| 2 | Check the food against the collision lecture | Compare the food with the lecture on collisions with food: a blue circle of 10 by 10 pixels (`FOOD_SIZE` 0.5), a random place from the `random` module that is never at the edge of the screen, `refresh` at creation and at every collision, and the eating distance of less than 15 pixels. Write the result as rows of the comparison table. | No | |
| 3 | Check the scoreboard against its lecture | Compare the scoreboard with the lecture: the score starts at 0, the text is written with alignment and font taken from constants, the turtle is hidden, `increase_score` adds 1, and `update_scoreboard` clears the old text before it writes the new one. Write the result as rows of the comparison table. | No | |
| 4 | Check the wall and the game-over text against their lecture | Compare the wall and the end of the game with the lecture: the wall is at 280 and -280 on both axes, passing it sets `game_is_on` to false, and GAME OVER is shown in the middle with the score still visible. Write the result as rows of the comparison table. | No | |
| 5 | Check growth and the tail against their lecture | Compare `extend`, `add_segment` and the tail check with the lecture: `extend` adds a segment at the position of the last segment, and the head touches the tail below 10 pixels with the head itself skipped. Write the result as rows of the comparison table. | No | |
| 6 | Correct the code where it differs from the lectures | For every row of the comparison table marked different, change the constant or the code, add or change the test that proves it, and say so in the pull request. If no row differs, change no source file and state that in the pull request. | No | |
| 7 | Finish the README for the Day 21 repository | Rewrite the Status and Run sections of `README.md` for the whole game (moving, food, score, game over, closing), remove every sentence that is out of date, update the Project layout, and confirm that `doxygen Doxyfile` ends with 0 warnings and that a fresh clone reaches a green `pytest` by following the README. | No | |
| 8 | Check the repository page and compare with the video | Check on the git host that the description and at least 5 topics are still set, run the finished game next to the lecture video, and write every difference in the pull request. | No | |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-002]: ./mil-002-adopt-the-game.md
