import random
from tkinter import *
import pandas
from pathlib import Path

BACKGROUND_COLOR = "#B1DDC6"
FIRST_FONT = ("Ariel", 40, "italic")
SECOND_FONT = ("Ariel", 60, "bold")
WORDS_FILE = Path("data/words_to_learn.csv")
DEFAULT_FILE = Path("data/french_words.csv")

current_card = {}
flip_timer = None

def load_default_words():
    global data, using_words_to_learn
    if WORDS_FILE.exists():
        df = pandas.read_csv(WORDS_FILE, encoding="utf-8")
        data = df.to_dict(orient="records")
        using_words_to_learn = True
    else:
        df = pandas.read_csv(DEFAULT_FILE, encoding = "utf-8")
        data = df.to_dict(orient="records")
        using_words_to_learn = False

load_default_words()

def next_card():
    global current_card, flip_timer
    if not data:
        return

    if flip_timer:
        screen.after_cancel(flip_timer)

    current_card = random.choice(data)
    canvas.itemconfig(card_image, image=card_front_img)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word_original, text=current_card["French"], fill="black")

    flip_timer = screen.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_image, image=card_back_img)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word_original, text=current_card["English"], fill="white")

def add_wrong_word():
    if using_words_to_learn:
        next_card()
        return

    if WORDS_FILE.exists():
        df = pandas.read_csv(WORDS_FILE)
        words = df.to_dict(orient="records")
    else:
        words = []

    if current_card not in words:
        words.append(current_card)

    pandas.DataFrame(words).to_csv(WORDS_FILE, index=False)
    next_card()

def remove_right_word():
    global data
    if not using_words_to_learn:
        next_card()
        return

    data.remove(current_card)

    if len(data) == 0:
        WORDS_FILE.unlink()
        load_default_words()
    else:
        pandas.DataFrame(data).to_csv(WORDS_FILE, index=False)

    next_card()

#################### UI ####################
screen = Tk()
screen.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
screen.title("Flashy")
screen.resizable(False, False)
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)

card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

card_image = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)

language = canvas.create_text(400, 150, text="French", font=FIRST_FONT)
word_original = canvas.create_text(400, 263, text="", font=SECOND_FONT)

wrong_button = Button(image=wrong_img, highlightthickness=0, command=add_wrong_word)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_img, highlightthickness=0, command=remove_right_word)
right_button.grid(row=1, column=1)


next_card()
screen.mainloop()