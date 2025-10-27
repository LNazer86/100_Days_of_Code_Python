import random
from time import sleep
import hangman_art
import hangman_words

lives = len(hangman_art.stages) - 1
guessed_letters = []

print(hangman_art.logo)
print(hangman_art.stages[lives])

chosen_word = random.choice(hangman_words.word_list)
user_word = ["_"] * len(chosen_word)
print(user_word)

while lives > 0:
    user_letter = input("Guess a letter: ").lower()

    if user_letter in chosen_word:
        for index, char in enumerate(chosen_word):
            if char == user_letter:
                user_word[index] = char
        print("".join(user_word))

        if "_" not in user_word:
            print(f"You guessed all letters. The word was {chosen_word}. YOU WIN!")
            sleep(5)
            break
    else:
        if user_letter in guessed_letters:
            print("You already guess this letter!")
        else:
            if lives > 1:
                lives -= 1
                print(hangman_art.stages[lives])
                print(f"Wrong guess. You lose a life. Your lives: {lives}")
                print("".join(user_word))
                guessed_letters.append(user_letter)
            else:
                print(hangman_art.stages[0])
                print("You lost all lives. GAME OVER!")
                print(f"The word was {chosen_word}.")
                sleep(5)
                break




