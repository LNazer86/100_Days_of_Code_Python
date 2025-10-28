import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)
repeat = True

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            encrypted_text += alphabet[index + shift]
        else:
            encrypted_text += char
    print(encrypted_text)


def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char in alphabet:
           index = alphabet.index(char)
           decrypted_text += alphabet[index - shift]
        else:
            decrypted_text += char
    print(decrypted_text)


while repeat:
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt: \n").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type your shift number: \n")) % 26

    if direction.lower() == "encode":
        encrypt(text, shift)
        message = input("Do you want to continue? Type 'y' for continue or 'n' to exit: \n").lower()
        if message == "y":
            continue
        elif message == "n":
            repeat = False
        else:
            print("Wrong input")

    elif direction.lower() == "decode":
        decrypt(text, shift)
        message = input("Do you want to continue? Type 'y' for continue or 'n' to exit: \n").lower()
        if message == "y":
            continue
        elif message == "n":
            repeat = False
        else:
            print("Wrong input")

    else:
        print("Wrong direction!")