# 🪓 Hangman (Python)

Jednoduchá konzolová hra Hangman, kterou jsem vytvořil během učení Pythonu.  
Cílem projektu bylo procvičit si cykly, podmínky, práci se seznamy a manipulaci s řetězci.

## 🎯 Funkce hry
- Náhodně se vygeneruje tajné slovo.
- Hráč hádá po jednotlivých písmenech.
- Každý špatný pokus ubírá život a zobrazuje část věšáku.
- Pokud hráč uhodne všechna písmena, hra končí výhrou.
- Pokud dojdou všechny životy, zobrazí se „GAME OVER“.

## 🧠 Co jsem si na tom procvičil
- Práci s `while` cyklem a `for` smyčkou.
- Použití podmínek `if / else`.
- Seznamy (`list`), jejich indexy a nahrazování znaků.
- Modul `random` pro výběr náhodného slova.
- Základy importování vlastních modulů.

## ▶️ Spuštění hry
K běhu potřebuješ Python 3.  
Stáhni si všechny tři soubory (`main.py`, `hangman_art.py`, `hangman_words.py`) do jedné složky a spusť:

```bash
python main.py
```

## 🧩 Soubory v projektu
- **main.py** – hlavní logika hry  
- **hangman_art.py** – ASCII obrázky věšáku  
- **hangman_words.py** – seznam slov, ze kterých hra náhodně vybírá

## 💬 Poznámka
Tento projekt slouží pro výuku a trénink základů Pythonu.  
Postupně ho plánuji vylepšovat (např. přidat funkce, GUI nebo skóre).
