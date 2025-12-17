# Flashcard App – French ↔ English

Jednoduchá desktopová aplikace v Pythonu pro učení slovíček pomocí **flashcards**.
Aplikace zobrazuje francouzské slovo, po krátké pauze jej automaticky otočí a zobrazí anglický překlad.

Uživatel si může označit slova, která **zná** nebo **nezná** – aplikace si pamatuje postup učení.

---

## Funkce aplikace
- náhodný výběr slovíček
- automatické otočení karty po 3 sekundách
- ukládání slov k procvičení do `words_to_learn.csv`
- mazání naučených slov ze seznamu
- návrat k původnímu slovníku po dokončení učení
- grafické rozhraní pomocí **Tkinter**
- práce se soubory CSV přes **pandas**
- kontrola existence souborů (`Path`, `exists()`)

---

## Použité technologie
- Python 3
- Tkinter (GUI)
- pandas (práce s CSV)
- pathlib (správa souborů)
- random

---

## Spuštění
```bash
python main.py
```

---

## O projektu
Projekt byl vytvořen jako součást kurzu  
**100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu (Day 31)**.

Cílem bylo procvičit:
- práci s grafickým rozhraním (Tkinter),
- práci s daty v CSV souborech,
- ukládání stavu aplikace mezi spuštěními,
- logiku aplikace založenou na uživatelských akcích,
- strukturování většího projektu.
