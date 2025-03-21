
import turtle
import pandas as pd

from cursor import Cursor

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

cursor = Cursor()

df= pd.read_csv("50_states.csv")
states_list = df["state"].to_list()

guess = screen.textinput("Guess the State", "Name another state")
formatted_guess = guess.title()

if formatted_guess in states_list:
    coordinates = df[df["state"] == formatted_guess]
    x = coordinates.x.to_list()[0]
    y = coordinates.y.to_list()[0]

    cursor.move_to(x,y)
    cursor.write_state(formatted_guess)

screen.exitonclick()
