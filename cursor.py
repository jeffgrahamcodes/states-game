from turtle import Turtle


class Cursor(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def move_to(self, x, y):
        self.goto(x,y)

    def write_state(self, state):
        self.write(state)
