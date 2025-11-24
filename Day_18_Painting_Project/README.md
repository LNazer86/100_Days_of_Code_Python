# Hirst Dot Painting 🎨

Tento projekt vytváří mřížku barevných teček inspirovanou dílem Damiena Hirsta.
Program používá knihovnu `turtle` a předdefinovaný seznam RGB barev.

## Jak to funguje
- želva začíná vlevo dole  
- vykreslí 10 řádků po 10 tečkách  
- každá tečka má náhodnou barvu ze seznamu `color_list`  
- pohyb mezi tečkami je řízen pevnými offsety

## Hlavní části kódu
- `color_list` – seznam RGB barev  
- smyčky pro vykreslování řádků a sloupců  
- `turtle.colormode(255)` pro podporu RGB barev  
- rychlé vykreslování přes `speed("fastest")`

## O projektu
Projekt byl vytvořen jako součást kurzu **100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu (Day 18)**.
Cílem bylo procvičit práci s knihovnou `turtle`, cykly a řízení pozice na obrazovce.
