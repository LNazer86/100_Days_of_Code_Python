import art
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def start_game():
    while True:
        start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if start == "y":
            os.system("cls" if os.name == "nt" else "clear")
            print(art.logo)
            game()
        elif start == "n":
            print("See you soon. Bye!")
            break
        else:
            print("Invalid input. Type only 'y' or 'n'.")


def game():
    user_cards = []
    com_cards = []

    user_cards.append(random.choice(cards))
    user_cards.append(random.choice(cards))
    com_cards.append(random.choice(cards))
    com_cards.append(random.choice(cards))

    # Ace (11) can also count as 1 if needed
    while 11 in user_cards and sum(user_cards) > 21:
        user_cards[user_cards.index(11)] = 1

    while 11 in com_cards and sum(com_cards) > 21:
        com_cards[com_cards.index(11)] = 1

    print(f"Your cards: {user_cards}")
    print(f"Computer first card: {com_cards[0]}")

    while True:
        user_score = sum(user_cards)
        com_score = sum(com_cards)

        if user_score == 21 and len(user_cards) == 2:
            print("Blackjack! You win!\n")
            return

        while 11 in user_cards and sum(user_cards) > 21:
            user_cards[user_cards.index(11)] = 1
            user_score = sum(user_cards)

        another_card = input("Type 'y' to get another card or type 'n' to pass: ").lower()
        if  another_card == 'y':
            user_cards.append(random.choice(cards))
            user_score = sum(user_cards)

            while 11 in user_cards and user_score > 21:
                user_cards[user_cards.index(11)] = 1
                user_score = sum(user_cards)

            print(f"Your next card: {user_cards[-1]}, your total score: {user_score}")

            if user_score > 21:
                print("You are over 21. You lose!\n")
                return
            if com_score == 21 and user_score == 21:
                print("It's a draw!\n")
                return

        elif another_card == 'n':
            if com_score == 21 and len(com_cards) == 2:
                print(f"Computer's cards: {com_cards}\nComputer have Blackjack! You lose!")
            else:
                print(f"Computer's cards: {com_cards}")
                while com_score < 17:
                    com_cards.append(random.choice(cards))
                    com_score = sum(com_cards)
                    while 11 in com_cards and com_score > 21:
                        com_cards[com_cards.index(11)] = 1
                        com_score = sum(com_cards)
                    print(f"Computer's next card: {com_cards[-1]}, computer's total score: {com_score}")
                    if com_score > 21:
                        print(f"Computer is over 21. You win!\n")
                        return

            if user_score == com_score:
                print("It's a draw!\n")
                return
            else:
                if user_score <= 21 and user_score > com_score:
                    print(f"Your total score: {user_score}, computer's total score: {com_score}")
                    print("You win!\n")
                    return
                else:
                    print(f"Your total score: {user_score}, computer's total score: {com_score}")
                    print("You lose!\n")
                    return
        else:
            print("Wrong input!")



start_game()
print(art.logo)
