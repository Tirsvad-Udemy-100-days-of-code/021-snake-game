> This page is generated from README.md and wiki/. Changes made here are overwritten the next time the wiki is published.

English | [Dansk](Home.da) | [Bahasa Melayu](Home.ms)

# Snake Game (Day 21)

The classic Snake game, built object-oriented with Python's `turtle` module. It is the day-21 assignment of Udemy's *100 Days of Code: The Complete Python Pro Bootcamp*: a snake moves across a black 600 by 600 screen by itself and is steered with the arrow keys; it eats food, grows, and a score is shown at the top. The game is over when the head passes the wall or touches its own tail.

![The game at a score of 5: a light green snake with a dark green head and a mouth, blue food and the score at the top](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/021-snake-game/raw/branch/main/docs/images/snake-score-5.png)

*The running game at a score of 5: a light green body, a dark green head with a mouth, the blue food and the white score.*

## Controls

| Key | Effect |
| --- | --- |
| Up, Down, Left, Right | Turn the snake |

The snake never turns straight back onto itself. When the head comes closer than 15 pixels to the blue food the snake eats it, grows by one segment and the score goes up by 1.

## Run

Python 3.13 or newer with `tkinter` is needed; the game has no other runtime dependencies.

```bash
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/021-snake-game.git
cd 021-snake-game
python -m pip install -e .
python -m snake_game
```

The README of the repository has the full set-up for Windows, Linux and macOS.
