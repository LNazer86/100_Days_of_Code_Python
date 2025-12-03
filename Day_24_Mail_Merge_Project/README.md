# Mail Merge – Generování dopisů (Python)

Jednoduchý Python skript pro automatické generování personalizovaných dopisů ze šablony. Program načte seznam jmen, nahradí zástupný text ve vzoru dopisu a pro každé jméno vytvoří samostatný soubor.

## Funkce
- Načtení seznamu jmen ze souboru
- Nahrazení zástupného textu `[name]` skutečným jménem
- Vytvoření samostatného dopisu pro každého příjemce
- Uložení výsledných dopisů do složky `ReadyToSend`

## Struktura projektu
- Input/Names/invited_names.txt`
- Input/Letters/starting_letter.txt`
- Output/ReadyToSend/`

## Spuštění
python main.py

## O projektu
Projekt byl vytvořen jako součást kurzu  
**100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu**.  
Cílem bylo procvičit práci se soubory, čtení a zápis dat a nahrazování textu pomocí metody replace().
