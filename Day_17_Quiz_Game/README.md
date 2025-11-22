# Quiz Game – Python OOP Projekt

Tento projekt je jednoduchá konzolová kvízová aplikace vytvořená v rámci učení Pythonu.
Slouží k procvičení základních principů objektově orientovaného programování (OOP):

- tvorba tříd
- konstruktor a atributy
- metody
- práce s více soubory
- importy a modulární struktura

Projekt vychází z výukového kurzu a jeho účelem je posílit porozumění OOP a strukturovanému psaní kódu.

---

## Jak aplikace funguje

Aplikace načte seznam otázek a postupně je uživateli pokládá. Každá otázka má odpověď typu
**True / False**.

Program:

1. zobrazí otázku
2. načte uživatelovu odpověď
3. vyhodnotí ji
4. přičte skóre, pokud byla správná
5. na konci vypíše celkový výsledek

---

## Struktura projektu

```
.
├── data.py               # seznam otázek a odpovědí
├── main.py               # hlavní smyčka programu
├── question_model.py     # třída Question
├── quiz_brain.py         # logika kvízu v samostatné třídě
└── README.md             # dokumentace projektu
```

---

## Použité technologie

- Python 3
- Objektově orientované programování
- Modulární struktura kódu

---

## Jak spustit aplikaci

1. Stáhněte nebo naklonujte repozitář
2. Otevřete projekt v IDE (PyCharm, VS Code, …)
3. Spusťte soubor `main.py`
4. Odpovídejte na otázky v konzoli

---

## Účel projektu

Projekt je součástí mé studijní cesty při učení Pythonu.
Slouží k pochopení OOP a jako trénink při práci s třídami, objekty a logikou programu.
