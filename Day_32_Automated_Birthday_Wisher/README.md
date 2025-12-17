
# Birthday Email Sender 🎂✉️

Python skript, který **automaticky odešle přání k narozeninám e‑mailem** v den narozenin osoby uložené v CSV souboru.

## Jak to funguje
- Načte dnešní datum
- Zkontroluje, zda má někdo dnes narozeniny
- Náhodně vybere text přání
- Odešle e‑mail přes SMTP server

## Struktura projektu
- `main.py` – hlavní skript
- `birthdays.csv` – seznam narozenin
- `letter_templates/` – textové šablony přání

## Formát CSV souboru
Sloupce musí být přesně v tomto pořadí:
- name
- email
- year
- month
- day

## Použité technologie
- Python
- pandas
- smtplib
- datetime

## O projektu
Projekt byl vytvořen jako součást kurzu **100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu**.  
Cílem bylo procvičit práci se soubory CSV, slovníky, datem a odesíláním e‑mailů.
