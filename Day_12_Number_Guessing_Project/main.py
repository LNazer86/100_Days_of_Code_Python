import random
import art
import os

print("Welcome to the Number Guessing Game!")

def attempts():
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if difficulty.lower() == "easy":
            return 10
        elif difficulty.lower() == 'hard':
            return 5
        else:
            print("Incorrect input!")

def game():
    print(art.logo)
    random_number = random.randint(1, 100)
    remaining_attempts = attempts()
    player_guesses = []

    while remaining_attempts > 0:
        print(f"You have {remaining_attempts} attempts remaining to guess the number.")
        player_input = input("Make a guess: ")

        if not player_input.isdigit():
            print("You can input only numbers 1-100.")
        elif int(player_input) < 1 or int(player_input) > 100:
            print("You can input only numbers 1-100.")
        else:
            number = int(player_input)

            if number in player_guesses:
                print("You already guessed this number. Try again.")
            else:
                if remaining_attempts == 1:
                    if number > random_number:
                        print(f"Too high.\nYou've run out of guesses, you lose.\nThe answer was {random_number}.")
                        break
                    elif number < random_number:
                        print(f"Too low.\nYou've run out of guesses, you lose.\nThe answer was {random_number}.")
                        break
                    else:
                        print(f"You got it! The answer was {random_number}.")
                        break
                else:
                    if number > random_number:
                        print("Too high.\nGuess again.")
                        remaining_attempts -= 1
                        player_guesses.append(number)
                    elif number < random_number:
                        print("Too low.\nGuess again.")
                        remaining_attempts -= 1
                        player_guesses.append(number)
                    else:
                        print(f"You got it! The answer was {random_number}.")
                        break

game()
while True:
    repeat = input("Do you want to play again? 'y' or 'n': ").lower()
    if repeat == "n":
        print("Thank you for game. Bye!")
        break
    elif repeat == "y":
        os.system("cls" if os.name == "nt" else "clear")
        game()
    else:
        print("Invalid input!")

