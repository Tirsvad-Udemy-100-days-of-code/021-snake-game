> Denne side er genereret fra README.md og wiki/. Ændringer her bliver overskrevet, næste gang wikien udgives.

> Den engelske side er den gældende; denne oversættelse følger den.

[English](Home) | Dansk | [Bahasa Melayu](Home.ms)

# Snake-spillet (dag 21)

Det klassiske Snake-spil, bygget objektorienteret med Pythons `turtle`-modul. Det er opgaven fra dag 21 i Udemys *100 Days of Code: The Complete Python Pro Bootcamp*: en slange bevæger sig af sig selv hen over en sort skærm på 600 gange 600 og styres med piletasterne; den spiser mad, vokser, og en score vises øverst. Spillet er slut, når hovedet passerer væggen eller rører sin egen hale.

![Spillet ved en score på 5: en lysegrøn slange med et mørkegrønt hoved og en mund, blå mad og scoren øverst](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/021-snake-game/raw/branch/main/docs/images/snake-score-5.png)

*Det kørende spil ved en score på 5: en lysegrøn krop, et mørkegrønt hoved med en mund, den blå mad og den hvide score.*

## Styring

| Tast | Virkning |
| --- | --- |
| Op, Ned, Venstre, Højre | Drejer slangen |

Slangen vender aldrig direkte om på sig selv. Når hovedet kommer tættere end 15 pixels på den blå mad, spiser slangen den, vokser med ét led, og scoren stiger med 1.

## Kør spillet

Der skal bruges Python 3.13 eller nyere med `tkinter`; spillet har ingen andre afhængigheder ved kørsel.

```bash
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/021-snake-game.git
cd 021-snake-game
python -m pip install -e .
python -m snake_game
```

Repositoriets README har den fulde opsætning til Windows, Linux og macOS.
