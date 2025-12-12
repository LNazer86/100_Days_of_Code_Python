# Správce hesel — Tkinter aplikace

Tento projekt je jednoduchý správce hesel vytvořený v Pythonu pomocí knihovny **Tkinter**.

Aplikace umožňuje:
- generovat bezpečná hesla,
- kopírovat heslo automaticky do schránky,
- ukládat hesla spolu s webem a e‑mailem do textového souboru,
- zobrazovat varování a potvrzovací dialogy.

---

## Funkce

### 🔐 Generátor hesel
- Kombinuje písmena, čísla a symboly.
- Délka hesla je náhodná.
- Vygenerované heslo se automaticky kopíruje do schránky.

### 💾 Ukládání hesel
- Ukládá do souboru `data.txt` ve formátu:
  ```
  website | email | password
  ```
- Ověřuje, zda nejsou pole prázdná.
- Vyžaduje potvrzení před uložením.

### 🖼️ Uživatelské rozhraní
- Vytvořeno pomocí Tkinteru.
- Obsahuje vstupní pole, tlačítka a logo.
- Okno má pevnou velikost (resizable False).

---

## O projektu
Projekt byl vytvořen jako součást kurzu  
**100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu (Day 29)**.  
Cílem bylo procvičit Tkinter, práci se soubory a generování hesel.

