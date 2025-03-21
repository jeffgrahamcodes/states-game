
import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("50_states.csv")
all_states = df["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(f"{len(guessed_states)}/50 States Correct", "Name another state").title()

    if answer_state == "Exit":
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)


missed_states = {"state": []}
for state in all_states:
    if state not in guessed_states:
        missed_states["state"].append(state)

missed_states_df = pd.DataFrame(missed_states)
missed_states_df.to_csv("states_to_learn.csv")


