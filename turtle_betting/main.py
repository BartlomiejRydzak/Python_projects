from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
turtles = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

bet = screen.textinput(title="Make your bet", prompt="Choose color")

for i in range(6):
    turtles.append(Turtle(shape="turtle"))
    turtles[i].color(colors[i])
    turtles[i].up()
    y_start=-75
    turtles[i].goto(x=-230, y=y_start + (i*30))

race_is_on = True
while race_is_on:
    for turtle in turtles:
        turtle.forward(random.randint(0,10))
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            race_is_on = False

if bet == winner:
    print(f"You've won! The winner was {winner}")
else:
    print(f"You've lost! The winner was {winner}")

screen.exitonclick()