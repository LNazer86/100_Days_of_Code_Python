# 🔼 Higher-Lower Game

Jednoduchá terminálová hra v Pythonu inspirovaná populární Higher-Lower hrou.  
Cílem je uhodnout, která z dvou celebrit má více sledujících na sociálních sítích.

## 🎮 Popis hry
- Na začátku se zobrazí dvě náhodné osobnosti (A a B).  
- Hráč tipuje, kdo má více sledujících – zadá **A** nebo **B**.  
- Pokud odpoví správně, získává bod a hra pokračuje – vítěz zůstává jako **A**, proti němu se vygeneruje nová osoba **B**.  
- Pokud odpoví špatně, hra končí a vypíše se konečné skóre.  
- Po skončení je možné hru restartovat.

## ⚙️ Spuštění
1. Otevři složku s projektem v terminálu.  
2. Spusť příkaz:  
   ```bash
   python3 main.py
   ```  
3. Hra se spustí v terminálu.

## 🧩 Použité moduly
- `random` – pro generování náhodných osobností  
- `os` – pro čištění obrazovky  
- `art` a `game_data` – vlastní soubory s ASCII grafikou a daty o osobnostech

## 🧠 O projektu
Projekt byl vytvořen jako součást kurzu **100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu (Day 14)**.  
Cílem bylo procvičit práci s funkcemi, cykly, seznamy, podmínkami a strukturováním herní logiky.
