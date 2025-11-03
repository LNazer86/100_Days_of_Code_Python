import art
import os

bidders = {}
highest_bid = 0
winner = ""

def logo():
    print(art.logo)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear") # příkaz cls pro windows, clear pro linux

def add_bidder():
    bidder_name = input("Input name of bidder: ")

    while True:
        bid_input = input("Input bid amount: ")
        if bid_input.isdigit():
            bid = int(bid_input)
            break
        else:
            print("You can enter only numbers!")

    bidders[bidder_name] = bid
    another_bidder = input("Is there another bidder who want to bid ('y'/'n')? ").lower()

    if another_bidder == "y":
        clear_screen()
        logo()
        return True
    elif another_bidder == "n":
        clear_screen()
        logo()
        return False
    else:
        print("Please enter either 'y' or 'n'")
        return True

logo()
while add_bidder():
    pass

for bidder in bidders:
    if bidders[bidder] >= highest_bid:
        winner = bidder
        highest_bid = bidders[bidder]


print(f"The winner is {winner} with amount {highest_bid}.")

