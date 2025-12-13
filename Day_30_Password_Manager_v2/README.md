# Password Manager v2(Tkinter)

Jednoduchá desktopová aplikace v Pythonu pro **generování, ukládání a vyhledávání hesel**.
Aplikace využívá grafické rozhraní **Tkinter** a ukládá data do souboru **JSON**.

---

## Funkce aplikace
- generování silných náhodných hesel
- automatické kopírování hesla do schránky
- ukládání údajů (web / email / heslo) do `data.json`
- vyhledávání uložených hesel podle názvu webu
- ošetření chyb pomocí `try / except`
  - chybějící soubor
  - neexistující záznam
  - prázdná pole

---

## Použité technologie
- Python 3
- Tkinter (GUI)
- JSON (ukládání dat)
- `pyperclip` (kopírování do schránky)

---

## Spuštění
```bash
python main.py
```

---

## O projektu
Projekt byl vytvořen jako součást kurzu  
**100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu (Day 29)**.

Cílem bylo procvičit:
- práci s GUI (Tkinter),
- práci se soubory ve formátu JSON,
- správu dat pomocí slovníků,
- ošetření výjimek (`try / except / else / finally`),
- strukturování větší aplikace.
