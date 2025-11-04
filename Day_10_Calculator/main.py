import art
import os


def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    if number2 == 0:
        return "Error! Cannot divide by zero!"
    return number1 / number2

def logo():
    print(art.logo)

def get_number(user_prompt):
    while True:
        value = input(user_prompt)
        if value.replace(".", "", 1).isdigit():
            return float(value)
        else:
            print("You can enter only numbers!")

def get_operation(user_promt):
    while True:
        operator = input(user_promt)
        if operator not in operations:
            print("Enter valid operator!")
        else:
            return operator

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

while True:
    logo()

    number1 = get_number("Input first number: ")
    print(f"+\n-\n*\n/")
    operation = get_operation("Pick an operation: ")
    number2 = get_number("Input next number: ")
    result = operations[operation](number1, number2)
    print(f"{number1} {operation} {number2} = {result}")

    another_operation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

    while another_operation == "y":
        number1 = result
        print(f"+\n-\n*\n/")
        operation = get_operation("Pick an operation: ")
        number2 = get_number("Input next number: ")
        result = operations[operation](number1, number2)
        print(f"{number1} {operation} {number2} = {result}")
        another_operation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

    if another_operation == "n":
        os.system("cls" if os.name == "nt" else "clear")
        continue
    else:
        print("Wrong input!")
        break






