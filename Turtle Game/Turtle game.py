from turtle import Turtle, Screen
import random as rand

is_race_on = False
turtle_scr = Screen()
turtle_scr.setup(width=500, height=400)
user_bet = turtle_scr.textinput(title="Make your bet?", prompt="Which turtle would win the race? pick a colour: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
yposition = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    turt = Turtle(shape="turtle")
    turt.penup()
    turt.goto(x=-240, y=-yposition[turtle_index])
    turt.color(colors[turtle_index])
    all_turtles.append(turt)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won, {winning_color} dominated the rest")
            else:
                print(f"You lost, the winner is {winning_color}")
        rand_distance = rand.randint(0, 10)
        turtle.forward(rand_distance)

turtle_scr.exitonclick()