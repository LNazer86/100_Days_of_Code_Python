import random
import art
import game_data
import os

correct_answers = 0

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def index():
    random_index_a = random.randint(0, len(game_data.data) - 1)
    random_index_b = random.randint(0, len(game_data.data) - 1)

    while random_index_b == random_index_a:
        random_index_b = random.randint(0, len(game_data.data) - 1)
    return random_index_a, random_index_b


def people_to_compare(person_a = None):
    index_a, index_b = index()

    if person_a is None:
        person_a = game_data.data[index_a]
    person_b = game_data.data[index_b]

    print(art.logo)

    if correct_answers > 0:
        print(f"You're right! Current score: {correct_answers}")
    print(f'Compare A: {person_a["name"]}, {person_a["description"]}, from {person_a["country"]}.')
    print(art.vs)
    print(f'Against B: {person_b["name"]}, {person_b["description"]}, from {person_b["country"]}.')

    return person_a, person_b


def compare():
    person_a, person_b = people_to_compare()
    global correct_answers

    while True:
        player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        if player_choice == "a":
            if person_a["follower_count"] > person_b["follower_count"]:
                correct_answers += 1
                clear_screen()
                person_a = person_b
                person_a, person_b = people_to_compare(person_a)
            else:
                print(f"Sorry, that's wrong. Final score: {correct_answers}.")
                break
        elif player_choice == "b":
            if person_b["follower_count"] > person_a["follower_count"]:
                correct_answers += 1
                clear_screen()
                person_a = person_b
                person_a, person_b = people_to_compare(person_a)
            else:
                print(f"Sorry, that's wrong. Final score: {correct_answers}.")
                break
        else:
            print("Wrong input! You can type only 'A' or 'B'.")


compare()
while True:
    repeat = input("Do you want play again? Type 'y' or 'n': ").lower()

    if repeat == "y":
        correct_answers = 0
        clear_screen()
        compare()
    elif repeat == "n":
        print("Thank you for game. Bye!")
        break
    else:
        print("Wrong input. You can type only 'y' or 'n'.")
        continue