import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=745, height=531)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image) # zpristupni gif pro turtle
turtle.shape(image)
turtle.penup()

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
state_x = data["x"]
state_y = data["y"]

writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

guessed_states = []
correct_states = 0
non_guessed_states = []

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{correct_states}/50 States Correct", prompt="What's another state's name?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        for state in states:
            if state not in guessed_states:
                non_guessed_states.append(state)
        new_data = pandas.DataFrame(non_guessed_states, columns=["Missed states"])
        new_data.to_csv("missed_states.csv")
        break

    if answer_state in states and answer_state not in guessed_states:
        state_index = states.index(answer_state)
        writer.goto(state_x[state_index], state_y[state_index])
        writer.write(arg=answer_state)
        correct_states += 1
        guessed_states.append(answer_state)

    if correct_states == 50:
        game_is_on = False

