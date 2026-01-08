# ISS Overhead Notifier 🛰️🌙

Python skript, který **pravidelně kontroluje polohu Mezinárodní vesmírné stanice (ISS)** a ověřuje, zda se nachází v blízkosti zadané polohy a zároveň je noc.  
Pokud jsou splněny obě podmínky, odešle **e‑mailové upozornění**.

## Jak to funguje
- Každých 60 sekund zjistí aktuální polohu ISS pomocí veřejného API
- Ověří čas východu a západu slunce pro zadanou polohu
- Zkontroluje, zda je ISS v blízkosti a zda je noc
- Pokud ano, odešle e‑mail s upozorněním

## Struktura projektu
- `main.py` – hlavní skript

## Použité technologie
- Python
- requests
- datetime
- smtplib
- time

## Nastavení
Před spuštěním je nutné v kódu doplnit:
- zeměpisnou šířku a délku (`MY_LAT`, `MY_LNG`)
- e‑mailovou adresu a heslo pro odesílání zpráv

Z bezpečnostních důvodů nejsou přihlašovací údaje součástí repozitáře.

## O projektu
Projekt byl vytvořen jako součást kurzu **100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu**.  
Cílem bylo procvičit práci s API, zpracování JSON dat, časovou logiku a základní automatizaci.
