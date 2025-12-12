from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = (
        [choice(letters) for _ in range(randint(8, 10))] +
        [choice(numbers) for _ in range(randint(2, 4))] +
        [choice(symbols) for _ in range(randint(2, 4))]
    )

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(index=0, string=password)
    pyperclip.copy(password) #vlozi heslo do schranky

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_text = website_entry.get()
    username_text = username_entry.get()
    password_text = password_entry.get()

    if len(website_text) == 0 or len(username_text) == 0 or len(password_text) == 0:
        messagebox.showwarning(title="Warning", message="You left some fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_text, message=f"These are the details entered: \nEmail: {username_text} "
                                                       f"\nPassword: {password_text} \nIs it OK to save?")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website_text} | {username_text} | {password_text}\n")

            website_entry.delete(first=0, last=END)
            username_entry.delete(first=0, last=END)
            password_entry.delete(first=0, last=END)

            username_entry.insert(0, "jmeno@email.cz")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Password Generator")
window.config(padx=30, pady=30)
window.resizable(False, False)

canvas = Canvas(width=200, height=200, highlightthickness=0)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(110, 100, image=pass_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=45, highlightthickness=0)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")
website_entry.focus()

username_entry = Entry(width=45, highlightthickness=0)
username_entry.grid(row=2, column=1, columnspan=2, sticky="w")
username_entry.insert(0, "jmeno@email.cz")

password_entry = Entry(width=28, highlightthickness=0)
password_entry.grid(row=3, column=1, sticky="w")

#Buttons
generate_button = Button(text="Generate Password", width=13, command=generate_password)
generate_button.grid(row=3, column=2, sticky="w")

add_button = Button(text="Add", width=42, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="w")

window.mainloop()