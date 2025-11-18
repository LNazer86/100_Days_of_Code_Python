from data import MENU, resources
import os, time

def check_resources(drink):
    for ingredient, amount in MENU[drink]["ingredients"].items():
        if resources[ingredient] < amount:
            print(f"Sorry, not enough {ingredient}.")
            return False
    return True

def update_resources(drink, money):
    for ingredient, amount in MENU[drink]["ingredients"].items():
        resources[ingredient] -= amount
    resources["money"] += money

def only_int(promt):
    while True:
        value = input(promt)
        if value.isdigit():
            return int(value)
        print("You can enter only whole numbers!")

def coin_check(drink):
    print("Please insert coins.")
    quarters = only_int("How many quarters?: ")
    dimes = only_int("How many dimes?: ")
    nickles = only_int("How many nickles?: ")
    pennies = only_int("How many pennies?: ")

    inserted = round(quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01, 2)
    drink_price = MENU[drink]["cost"]
    if inserted < drink_price:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        change = round(inserted - drink_price, 2)
        print(f"Here is {change} in change.")
        return drink_price

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

while True:
    user_order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_order == "report":
        for i in resources:
            print(f"{i}: {resources[i]}")
        continue
    elif user_order == "off":
        print("Bye!")
        time.sleep(2)
        clear_screen()
        quit()
    elif user_order not in MENU.keys():
        print("Wrong input!")
        time.sleep(2)
        clear_screen()
        continue
    else:
        drink = user_order
        if check_resources(drink):
            payment = coin_check(drink)
            if not payment:
                continue
            update_resources(drink, payment)
            print(f"Here is your {drink}. Enjoy!")
            time.sleep(2)
            clear_screen()