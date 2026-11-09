# BookBot

BookBot je jednoduchá konzolová aplikácia v Pythone na analýzu textov kníh. Načíta textový súbor a vypíše prehľad počtu slov a výskytov jednotlivých písmen.

## Čo aplikácia dokáže

- Načítať knihu alebo iný text zo súboru `.txt`.
- Spočítať slová v texte.
- Spočítať výskyty písmen bez rozlišovania veľkých a malých písmen.
- Zobraziť písmená zoradené od najčastejšieho po najmenej časté.

Všetko spracúva lokálne a výsledky zobrazuje v termináli.

## Spustenie

Potrebuješ nainštalovaný Python 3. Aplikácia nevyžaduje žiadne externé knižnice.

V priečinku projektu spusti:

```sh
python main.py books/frankenstein.txt
```

Na systémoch, kde sa Python spúšťa príkazom `python3`, použi namiesto `python` príkaz `python3`.

Môžeš zadať aj cestu k vlastnému textovému súboru:

```sh
python main.py "cesta/k/mojej knihe.txt"
```

## Priložené knihy

V priečinku `books` sú pripravené texty kníh:

- Frankenstein
- Moby Dick
- Pýcha a predsudok (Pride and Prejudice)

## O projekte

BookBot je môj prvý projekt z kurzu [Boot.dev](https://www.boot.dev), vytvorený na precvičenie základov Pythonu, práce so súbormi a spracovania textu.

