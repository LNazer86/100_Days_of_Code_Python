#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("Input/Names/invited_names.txt", mode="r") as file:
    text = file.readlines()
names = [item.strip() for item in text]

with open("Input/Letters/starting_letter.txt", mode="r") as letter:
    letter_text = letter.read()
    for name in names:
        new_letter_text = letter_text.replace("[name]", name)
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as new_letter:
            new_letter.write(new_letter_text)
